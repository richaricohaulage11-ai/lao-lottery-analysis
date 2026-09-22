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
