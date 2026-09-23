"""
backtest.py
-----------
Walk-forward backtest engine, generalized to any of the derived prize
categories (two_digit, three_digit, four_digit).

Design choices that matter for validity:
- Walk-forward only: a strategy predicting draw t only ever sees draws
  0..t-1 (`min_history` warm-up draws are skipped entirely). No lookahead.
- Every strategy is compared to a RandomBaseline control and to the
  theoretical fair-game expectation, with a binomial confidence interval
  on the observed hit count, so you can state whether an observed
  difference is or is not distinguishable from chance.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd
from scipy.stats import binomtest

from .strategies import Strategy, TARGET_DIGITS


# Real published payout multipliers, confirmed from the actual sanook.com
# page text (scraped debug log, 18/9/69): "เลข 4 ตัว ... คูณด้วย 6,000",
# "เลข 3 ตัว ... คูณด้วย 500", "เลข 2 ตัว ... คูณด้วย 60".
#
# "fair" here means the actuarially-neutral payout — exactly 1/probability
# for each category (100 for 2-digit, 1000 for 3-digit, 10000 for
# 4-digit) — i.e. what the payout WOULD be if there were no house edge.
# Comparing real vs. fair quantifies the built-in house edge directly:
# real=60 vs fair=100 for two_digit means a random bettor's expected ROI
# is (60/100 - 1) = -40% under the real payout table, vs 0% if it were
# fair. Same logic for three_digit: (500/1000 - 1) = -50%.
PAYOUT_SCENARIOS = {
    "real": {"two_digit": 60.0, "three_digit": 500.0, "four_digit": 6000.0},
    "fair": {"two_digit": 100.0, "three_digit": 1000.0, "four_digit": 10000.0},
}


@dataclass
class BacktestResult:
    strategy_name: str
    target_column: str
    n_draws: int
    k_numbers: int
    stake_per_number: float
    payout_multiplier: float
    hits: int
    hit_rate: float
    expected_hit_rate: float
    total_staked: float
    total_returned: float
    roi_pct: float
    ci_low: float
    ci_high: float
    cumulative_bankroll: list[float] = field(repr=False, default_factory=list)

    def beats_baseline_significantly(self) -> bool:
        """True only if the theoretical expected hit rate falls OUTSIDE
        this strategy's 95% confidence interval — i.e. a genuine,
        statistically distinguishable deviation, not noise."""
        return not (self.ci_low <= self.expected_hit_rate <= self.ci_high)

    def __str__(self) -> str:
        verdict = (
            "statistically distinguishable from the random baseline"
            if self.beats_baseline_significantly()
            else "NOT statistically distinguishable from the random baseline "
            "(consistent with no real edge)"
        )
        return (
            f"[{self.strategy_name} on {self.target_column}] draws={self.n_draws}, "
            f"k={self.k_numbers}, hits={self.hits}/{self.n_draws} ({self.hit_rate:.2%}), "
            f"expected under fairness={self.expected_hit_rate:.2%}, "
            f"95% CI=({self.ci_low:.2%}, {self.ci_high:.2%}), "
            f"ROI={self.roi_pct:+.1f}% -> {verdict}"
        )


def run_backtest(
    df: pd.DataFrame,
    strategy: Strategy,
    min_history: int = 30,
    stake_per_number: float = 1.0,
    payout_multiplier: float = 90.0,
) -> BacktestResult:
    """Run one strategy walk-forward across the dataset for its target column."""
    if len(df) <= min_history:
        raise ValueError("Not enough draws for the requested min_history warm-up")

    target = strategy.target_column
    universe_size = 10 ** TARGET_DIGITS[target]

    hits = 0
    n_bets = 0
    bankroll = 0.0
    cumulative_bankroll = []

    k = strategy.k
    total_stake_per_draw = k * stake_per_number

    for i in range(min_history, len(df)):
        history = df.iloc[:i]
        actual = df.iloc[i][target]

        predicted = strategy.predict(history)
        n_bets += 1

        if actual in predicted:
            hits += 1
            bankroll += payout_multiplier * stake_per_number - total_stake_per_draw
        else:
            bankroll -= total_stake_per_draw

        cumulative_bankroll.append(bankroll)

    hit_rate = hits / n_bets
    expected_hit_rate = k / universe_size

    total_staked = n_bets * total_stake_per_draw
    total_returned = hits * payout_multiplier * stake_per_number
    roi_pct = (total_returned - total_staked) / total_staked * 100.0

    ci = binomtest(hits, n_bets, p=expected_hit_rate).proportion_ci(confidence_level=0.95)

    return BacktestResult(
        strategy_name=strategy.name,
        target_column=target,
        n_draws=n_bets,
        k_numbers=k,
        stake_per_number=stake_per_number,
        payout_multiplier=payout_multiplier,
        hits=hits,
        hit_rate=hit_rate,
        expected_hit_rate=expected_hit_rate,
        total_staked=total_staked,
        total_returned=total_returned,
        roi_pct=roi_pct,
        ci_low=ci.low,
        ci_high=ci.high,
        cumulative_bankroll=cumulative_bankroll,
    )


def compare_strategies(
    df: pd.DataFrame,
    strategies: list[Strategy],
    min_history: int = 30,
    stake_per_number: float = 1.0,
    payout_multiplier: float = 90.0,
) -> list[BacktestResult]:
    return [
        run_backtest(df, strat, min_history=min_history, stake_per_number=stake_per_number,
                     payout_multiplier=payout_multiplier)
        for strat in strategies
    ]


def backtest_report(results: list[BacktestResult]) -> str:
    lines = ["# Backtest Report", ""]
    lines.append(
        "Every strategy is walk-forward (no lookahead) and compared to the "
        "theoretical fair-game expectation and to a random-baseline control. "
        "A strategy only has a demonstrated edge if its 95% confidence "
        "interval excludes the fair-game expected hit rate."
    )
    lines.append("")

    by_target: dict[str, list[BacktestResult]] = {}
    for r in results:
        by_target.setdefault(r.target_column, []).append(r)

    any_beats = False
    for target, target_results in by_target.items():
        lines.append(f"## Target: {target}")
        for r in target_results:
            lines.append(f"- {r}")
            if r.beats_baseline_significantly() and r.strategy_name != "random_baseline":
                any_beats = True
        lines.append("")

    lines.append("## Verdict")
    if any_beats:
        lines.append(
            "One or more non-baseline strategies showed a statistically "
            "significant deviation from the fair-game expectation in this "
            "sample. Given multiple strategies and targets were tested, "
            "check whether this survives correction for multiple "
            "comparisons and whether it replicates on an independent, "
            "later sample before drawing any conclusion — a single "
            "significant result among several tests is exactly what chance "
            "alone would occasionally produce."
        )
    else:
        lines.append(
            "No strategy showed a statistically significant edge over the "
            "fair-game expectation, on any target category. This is the "
            "result predicted by probability theory for a fair lottery, "
            "and matches findings in the peer-reviewed literature on other "
            "lotteries (see the companion research report)."
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------
# Small-sample backtest sensitivity (10-50 draws).
#
# Requested by the user's advisor: instead of one backtest on all
# available data, run the SAME backtest repeatedly on just the last N
# draws, for N = 10, 15, 20, ..., 50 — to see whether conclusions (hit
# rate, ROI) are stable across sample sizes, or bounce around due to
# small-sample noise. Distinct from the Fibonacci/golden-ratio window
# sensitivity in stats_analysis.py, which tests overall randomness
# (chi-square/entropy) rather than strategy performance.
#
# With only 10-50 draws and k candidate numbers per draw, statistical
# power here is very low — a handful of lucky/unlucky hits can swing the
# hit rate a lot. That is itself the point being demonstrated: small
# samples are noisy, which is why the main backtest requires >35 draws
# before drawing conclusions.
# ---------------------------------------------------------------------

def backtest_sensitivity_by_window(
    df: pd.DataFrame,
    strategy_classes: list,
    target_column: str = "two_digit",
    window_sizes: list[int] | None = None,
    k: int = 5,
    payout_multiplier: float = 90.0,
) -> list[dict]:
    """Runs a fresh walk-forward backtest on just the last N draws, for
    each window size N in `window_sizes` that the data can support.
    Returns a flat list of {window, strategy, n_bets, hit_rate,
    expected_hit_rate, roi_pct} dicts — one row per (window, strategy).
    """
    if window_sizes is None:
        window_sizes = [10, 15, 20, 25, 30, 35, 40, 45, 50]

    rows = []
    for w in window_sizes:
        if len(df) < w:
            continue
        sub_df = df.tail(w).reset_index(drop=True)
        min_hist = max(3, w // 4)
        if len(sub_df) <= min_hist + 2:
            continue  # not enough post-warmup draws to bet on at all

        strategies = [cls(target_column=target_column, k=k) for cls in strategy_classes]
        try:
            results = compare_strategies(
                sub_df, strategies, min_history=min_hist, payout_multiplier=payout_multiplier
            )
        except ValueError:
            continue

        for r in results:
            rows.append({
                "window": w,
                "strategy": r.strategy_name,
                "n_bets": r.n_draws,
                "hit_rate": r.hit_rate,
                "expected_hit_rate": r.expected_hit_rate,
                "roi_pct": r.roi_pct,
            })

    return rows


# ---------------------------------------------------------------------
# k-sensitivity (how many numbers to bet per draw) x payout scenario
# (real published rates vs. actuarially-fair rates).
#
# Betting more numbers (larger k) does NOT change a random bettor's
# EXPECTED ROI — each additional number has the same per-unit expected
# value, so the theoretical expectation is flat in k. What changes is
# the VARIANCE: more numbers means more independent bets per draw, so
# the realized hit rate converges faster to its true expected value
# (law of large numbers) and swings less wildly. This function makes
# that visible empirically, across both the real and fair payout tables.
# ---------------------------------------------------------------------

def k_and_payout_sensitivity(
    df: pd.DataFrame,
    strategy_classes: list,
    target_column: str = "two_digit",
    k_values: list[int] | None = None,
    min_history: int = 30,
    stake_per_number: float = 1.0,
) -> dict:
    """Runs the full backtest across every combination of k (numbers bet
    per draw) and payout scenario ('real' vs 'fair'). Returns
    {scenario_name: [{k, strategy, n_bets, hit_rate, expected_hit_rate,
    roi_pct, ci_low, ci_high, significant}, ...]}.
    """
    if k_values is None:
        universe_size = 10 ** TARGET_DIGITS[target_column]
        k_values = [k for k in [1, 3, 5, 10, 20] if k < universe_size]

    output: dict[str, list[dict]] = {}
    for scenario_name, payout_by_target in PAYOUT_SCENARIOS.items():
        payout = payout_by_target[target_column]
        rows = []
        for k in k_values:
            strategies = [cls(target_column=target_column, k=k) for cls in strategy_classes]
            try:
                results = compare_strategies(
                    df, strategies, min_history=min_history,
                    stake_per_number=stake_per_number, payout_multiplier=payout,
                )
            except ValueError:
                continue
            for r in results:
                rows.append({
                    "k": k,
                    "strategy": r.strategy_name,
                    "n_bets": r.n_draws,
                    "hit_rate": r.hit_rate,
                    "expected_hit_rate": r.expected_hit_rate,
                    "roi_pct": r.roi_pct,
                    "ci_low": r.ci_low,
                    "ci_high": r.ci_high,
                    "significant": r.beats_baseline_significantly(),
                })
        output[scenario_name] = rows

    return output
