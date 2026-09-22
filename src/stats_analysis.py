"""
stats_analysis.py
------------------
Randomness tests for a single 4-digit-per-draw lottery, where every
reported sub-prize (3/2 ตัว) is a trailing slice of the same 4-digit
number (see data_loader.py docstring).

Two families of test are computed, and they answer different questions:

1. Per-digit-position marginal tests (d0..d3): is each digit position, on
   its own, uniformly distributed 0-9?
2. Joint / interaction tests on two_digit, three_digit, and four_digit
   itself: even if every digit position is individually uniform, a GROUP
   of them could still be non-uniform if the positions are correlated
   with each other. Testing the joint frequency catches that —
   legitimate extra information, not double-counting.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.stats import chisquare, norm


@dataclass
class ChiSquareResult:
    label: str
    n_categories: int
    n_observations: int
    statistic: float
    p_value: float
    alpha: float = 0.05
    low_expected_count_warning: bool = False

    @property
    def significant(self) -> bool:
        return self.p_value < self.alpha

    def __str__(self) -> str:
        verdict = (
            "significant deviation from uniform (p < {:.2f})".format(self.alpha)
            if self.significant
            else "consistent with uniform (fails to reject randomness)"
        )
        warn = " [LOW SAMPLE WARNING: expected count per category < 5]" if self.low_expected_count_warning else ""
        return (
            f"{self.label}: chi2={self.statistic:.3f}, p={self.p_value:.4f}, "
            f"n={self.n_observations}, categories={self.n_categories} -> {verdict}{warn}"
        )


def _chi_square_from_counts(label: str, counts: pd.Series, alpha: float) -> ChiSquareResult:
    n = int(counts.sum())
    n_cat = len(counts)
    expected_per_cat = n / n_cat
    stat, p = chisquare(counts.values)
    return ChiSquareResult(
        label=label, n_categories=n_cat, n_observations=n,
        statistic=float(stat), p_value=float(p), alpha=alpha,
        low_expected_count_warning=expected_per_cat < 5,
    )


def digit_position_frequency(df: pd.DataFrame, position: int) -> pd.Series:
    """Frequency table (0-9) for digit position `position` (0=leftmost) of four_digit."""
    col = f"d{position}"
    counts = df[col].value_counts().reindex(range(10), fill_value=0).sort_index()
    counts.index.name = "digit"
    return counts


def chi_square_digit_position(df: pd.DataFrame, position: int, alpha: float = 0.05) -> ChiSquareResult:
    counts = digit_position_frequency(df, position)
    return _chi_square_from_counts(f"four_digit position {position} (marginal)", counts, alpha)


def group_frequency(df: pd.DataFrame, column: str, digits: int) -> pd.Series:
    """Frequency table for a trailing-digits column (two_digit/three_digit/four_digit)."""
    counts = df[column].value_counts()
    full_index = [f"{i:0{digits}d}" for i in range(10 ** digits)]
    counts = counts.reindex(full_index, fill_value=0)
    counts.index.name = column
    return counts


def chi_square_group(df: pd.DataFrame, column: str, digits: int, alpha: float = 0.05) -> ChiSquareResult:
    counts = group_frequency(df, column, digits)
    return _chi_square_from_counts(f"{column} ({digits} digits, joint/interaction test)", counts, alpha)


def runs_test(binary_sequence: list[int]) -> tuple[float, float]:
    x = np.asarray(binary_sequence)
    n1 = int((x == 1).sum())
    n0 = int((x == 0).sum())
    n = n1 + n0
    if n1 == 0 or n0 == 0:
        raise ValueError("Sequence must contain both 0s and 1s")
    runs = 1 + int(np.sum(x[1:] != x[:-1]))
    mean_runs = (2 * n1 * n0) / n + 1
    var_runs = (2 * n1 * n0 * (2 * n1 * n0 - n)) / (n**2 * (n - 1))
    z = (runs - mean_runs) / np.sqrt(var_runs)
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return float(z), float(p_value)


def odd_even_runs_test(df: pd.DataFrame, column: str) -> tuple[float, float]:
    values = df[column].astype(int)
    return runs_test((values % 2 == 0).astype(int).tolist())


def above_below_median_runs_test(df: pd.DataFrame, column: str) -> tuple[float, float]:
    values = df[column].astype(int)
    median = values.median()
    return runs_test((values > median).astype(int).tolist())


def autocorrelation(df: pd.DataFrame, column: str, nlags: int = 10) -> np.ndarray:
    from statsmodels.tsa.stattools import acf

    values = df[column].astype(int).to_numpy()
    values = (values - values.mean()) / values.std()
    result = acf(values, nlags=nlags, fft=True)
    return result[1:]


def full_randomness_report(df: pd.DataFrame, alpha: float = 0.05) -> str:
    lines = ["# Randomness Test Report", ""]
    lines.append(f"Draws analyzed: {len(df)}")
    lines.append(f"Date range: {df['draw_date'].min().date()} to {df['draw_date'].max().date()}")
    lines.append("")
    lines.append(
        "Reminder: every prize category below (5/4/3/2 ตัว) is a trailing "
        "slice of the SAME 4-digit draw (four_digit), not a separate random "
        "draw. See data_loader.py for exactly which digits map to which "
        "category."
    )
    lines.append("")

    lines.append("## Part 1: Marginal chi-square, per digit position of four_digit")
    sig_marginal = 0
    for pos in range(4):
        result = chi_square_digit_position(df, pos, alpha=alpha)
        lines.append(f"- {result}")
        if result.significant:
            sig_marginal += 1
    lines.append("")

    lines.append("## Part 2: Joint/interaction chi-square on the derived prize categories")
    joint_results = [
        chi_square_group(df, "two_digit", 2, alpha=alpha),
        chi_square_group(df, "three_digit", 3, alpha=alpha),
        chi_square_group(df, "four_digit", 4, alpha=alpha),
    ]
    sig_joint = 0
    for result in joint_results:
        lines.append(f"- {result}")
        if result.significant:
            sig_joint += 1
    lines.append("")

    lines.append("## Runs tests")
    min_for_runs = 10
    if len(df) < min_for_runs:
        lines.append(
            f"- Skipped: only {len(df)} draw(s) loaded, need at least "
            f"{min_for_runs} for a meaningful runs test. Will populate "
            f"automatically as more real draws are collected."
        )
    else:
        for column in ["two_digit", "three_digit"]:
            z_oe, p_oe = odd_even_runs_test(df, column)
            z_med, p_med = above_below_median_runs_test(df, column)
            lines.append(f"- {column} odd/even: z={z_oe:.3f}, p={p_oe:.4f} "
                         f"({'non-random ordering' if p_oe < alpha else 'consistent with random ordering'})")
            lines.append(f"- {column} above/below-median: z={z_med:.3f}, p={p_med:.4f} "
                         f"({'non-random ordering' if p_med < alpha else 'consistent with random ordering'})")
    lines.append("")

    lines.append("## Autocorrelation (lags 1-10)")
    min_for_acf = 15
    if len(df) < min_for_acf:
        lines.append(
            f"- Skipped: only {len(df)} draw(s) loaded, need at least "
            f"{min_for_acf} for a 10-lag autocorrelation. Will populate "
            f"automatically as more real draws are collected."
        )
    else:
        for column in ["two_digit", "three_digit"]:
            ac = autocorrelation(df, column, nlags=10)
            approx_ci = 1.96 / np.sqrt(len(df))
            n_outside = int((np.abs(ac) > approx_ci).sum())
            lines.append(f"- {column}: {n_outside}/10 lags outside the ~95% band "
                         f"(±{approx_ci:.3f}); ~0-1 expected by chance alone.")
    lines.append("")

    total_tests = 4 + len(joint_results)
    total_sig = sig_marginal + sig_joint
    lines.append("## Interpretation")
    lines.append(
        f"{total_sig} of {total_tests} chi-square tests were significant at "
        f"alpha={alpha}. With {total_tests} tests at alpha=0.05, roughly "
        f"{total_tests * 0.05:.1f} false positives are expected by chance "
        f"alone — a single isolated significant result is not strong "
        f"evidence of bias. A consistent pattern across positions, prize "
        f"categories, and separate time windows would be needed before "
        f"concluding the draw is not fair."
    )
    lines.append(
        "None of this measures predictability. A perfectly fair process can "
        "still show one 'significant' test out of several by chance — "
        "that is the expected multiple-testing effect, not a flaw."
    )

    return "\n".join(lines)


# ---------------------------------------------------------------------
# Additional methods: KS test, entropy, and time-based (month/year/
# weekday) homogeneity tests. These extend the randomness audit with
# more standard tools without changing its conclusions — a fair process
# should pass all of them, and any single "pattern" found across many
# tests is expected occasionally by chance (see the multiple-testing
# note above), not evidence of exploitable structure.
# ---------------------------------------------------------------------

@dataclass
class KSResult:
    label: str
    statistic: float
    p_value: float
    alpha: float = 0.05

    @property
    def significant(self) -> bool:
        return self.p_value < self.alpha

    def __str__(self) -> str:
        verdict = "significant deviation from uniform" if self.significant else "consistent with uniform"
        return f"{self.label}: D={self.statistic:.4f}, p={self.p_value:.4f} -> {verdict}"


def ks_test_uniform(df: pd.DataFrame, column: str, digits: int, alpha: float = 0.05) -> KSResult:
    """Kolmogorov-Smirnov goodness-of-fit vs. a continuous uniform
    distribution on [0, 10**digits). A second, distribution-shape-based
    check alongside chi-square (which only compares binned counts)."""
    from scipy.stats import kstest

    n_categories = 10 ** digits
    values = df[column].astype(int).to_numpy()
    stat, p = kstest(values, "uniform", args=(0, n_categories))
    return KSResult(label=f"{column} KS-test vs uniform[0,{n_categories})", statistic=float(stat), p_value=float(p), alpha=alpha)


def shannon_entropy_ratio(df: pd.DataFrame, column: str, digits: int) -> tuple[float, float, float]:
    """Returns (entropy_bits, max_entropy_bits, ratio). ratio close to 1.0
    means the distribution is close to maximally random (uniform); lower
    values indicate concentration in fewer outcomes than chance would
    produce."""
    counts = group_frequency(df, column, digits)
    total = counts.sum()
    if total == 0:
        return 0.0, 0.0, 0.0
    probs = counts[counts > 0] / total
    entropy = float(-np.sum(probs * np.log2(probs)))
    max_entropy = float(np.log2(len(counts)))
    ratio = entropy / max_entropy if max_entropy > 0 else 0.0
    return entropy, max_entropy, ratio


@dataclass
class HomogeneityResult:
    label: str
    group_col: str
    statistic: float
    p_value: float
    dof: int
    n_groups: int
    alpha: float = 0.05
    low_expected_count_warning: bool = False

    @property
    def significant(self) -> bool:
        return self.p_value < self.alpha

    def __str__(self) -> str:
        verdict = (
            f"distribution DIFFERS across {self.group_col} (p < {self.alpha})"
            if self.significant
            else f"distribution consistent across {self.group_col}"
        )
        warn = " [LOW SAMPLE WARNING]" if self.low_expected_count_warning else ""
        return (
            f"{self.label}: chi2={self.statistic:.3f}, p={self.p_value:.4f}, "
            f"dof={self.dof}, groups={self.n_groups} -> {verdict}{warn}"
        )


def chi_square_homogeneity(
    df: pd.DataFrame, digit_position: int, group_by: str, alpha: float = 0.05
) -> HomogeneityResult | None:
    """Tests whether a digit position's distribution (0-9) differs across
    groups defined by `group_by` ('month', 'year', or 'weekday') — i.e.
    does this position show a monthly/yearly/day-of-week pattern? Uses a
    contingency table + chi-square test of independence (not goodness-
    of-fit), since we're comparing groups to each other, not to a fixed
    uniform target.

    Returns None if there are fewer than 2 groups (test not meaningful).
    """
    from scipy.stats import chi2_contingency

    work = df.copy()
    if group_by == "month":
        work["_group"] = work["draw_date"].dt.strftime("%Y-%m")
    elif group_by == "year":
        work["_group"] = work["draw_date"].dt.year
    elif group_by == "weekday":
        work["_group"] = work["draw_date"].dt.day_name()
    else:
        raise ValueError(f"Unsupported group_by: {group_by}")

    if work["_group"].nunique() < 2:
        return None

    contingency = pd.crosstab(work["_group"], work[f"d{digit_position}"])
    # Ensure all 10 digit columns exist even if some never appeared
    for d in range(10):
        if d not in contingency.columns:
            contingency[d] = 0
    contingency = contingency[sorted(contingency.columns)]

    try:
        stat, p, dof, expected = chi2_contingency(contingency)
    except ValueError:
        # Too little data for scipy to even compute expected frequencies
        # (e.g. a row or column sums to zero) — not enough data yet.
        return None
    low_n = bool((expected < 5).any())

    return HomogeneityResult(
        label=f"four_digit position {digit_position} by {group_by}",
        group_col=group_by,
        statistic=float(stat),
        p_value=float(p),
        dof=int(dof),
        n_groups=work["_group"].nunique(),
        alpha=alpha,
        low_expected_count_warning=low_n,
    )


def monthly_series(df: pd.DataFrame, column: str) -> list[dict]:
    """Monthly mean of a numeric column, for a trend chart. Returns a
    list of {label, mean, count} dicts, one per calendar month present."""
    work = df.copy()
    work["_month"] = work["draw_date"].dt.strftime("%Y-%m")
    work["_val"] = work[column].astype(int)
    grouped = work.groupby("_month")["_val"].agg(["mean", "count"]).reset_index()
    return [
        {"label": row["_month"], "mean": float(row["mean"]), "count": int(row["count"])}
        for _, row in grouped.iterrows()
    ]


def extended_methods_report(df: pd.DataFrame, alpha: float = 0.05) -> str:
    """Extra methods beyond the core chi-square/runs/ACF audit: KS test,
    entropy, and month/year/weekday homogeneity — for a more thorough
    college research writeup."""
    lines = ["# Extended Methods Report", ""]

    lines.append("## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)")
    for column, digits in [("two_digit", 2), ("three_digit", 3), ("four_digit", 4)]:
        result = ks_test_uniform(df, column, digits, alpha=alpha)
        lines.append(f"- {result}")
    lines.append("")

    lines.append("## Shannon entropy (bits) vs. maximum possible entropy")
    lines.append("A ratio near 1.0 indicates the distribution is close to maximally random.")
    for column, digits in [("two_digit", 2), ("three_digit", 3)]:
        entropy, max_entropy, ratio = shannon_entropy_ratio(df, column, digits)
        lines.append(f"- {column}: entropy={entropy:.3f} bits, max={max_entropy:.3f} bits, ratio={ratio:.4f}")
    lines.append("")

    lines.append("## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)")
    for group_by in ["month", "year", "weekday"]:
        lines.append(f"### By {group_by}")
        any_result = False
        for pos in range(4):
            result = chi_square_homogeneity(df, pos, group_by, alpha=alpha)
            if result is not None:
                lines.append(f"- {result}")
                any_result = True
        if not any_result:
            lines.append(f"- Not enough distinct {group_by} groups yet to test.")
        lines.append("")

    lines.append(
        "Interpretation: these test whether the draw's digit distribution "
        "shifts across months, years, or days of the week — a legitimate "
        "question for a physical or electronic draw mechanism, distinct "
        "from testing overall uniformity. As with the core chi-square "
        "tests, isolated significant results among many groups/positions "
        "tested are expected by chance and are not evidence of a real "
        "time-based pattern unless they replicate consistently."
    )

    return "\n".join(lines)


# ---------------------------------------------------------------------
# Fibonacci / golden-ratio window-size sensitivity analysis.
#
# Idea: instead of running the randomness tests once on "all the data",
# run them on several different trailing-window sizes and see whether
# the conclusion (random vs. not) holds up across sample sizes. This is
# a standard robustness/sensitivity check.
#
# The window sizes used are Fibonacci numbers, chosen specifically
# because consecutive Fibonacci ratios F(n+1)/F(n) converge to the
# golden ratio phi (~1.6180339887) as n grows — a real, well-known
# mathematical property (not a numerology claim about lottery numbers).
# This gives geometrically-spaced sample sizes across the 10-400 range
# with a genuine golden-ratio justification for the spacing, which is
# different from (and more defensible than) claiming phi predicts draws.
# ---------------------------------------------------------------------

PHI = (1 + 5 ** 0.5) / 2  # ~1.6180339887...
_FIBONACCI_CANDIDATES = [13, 21, 34, 55, 89, 144, 233, 377]


def fibonacci_window_sizes(max_n: int, low: int = 10, high: int = 400) -> list[int]:
    """Fibonacci numbers in [low, high], capped at max_n (available draws).
    Always includes max_n itself (the full dataset) as the last point,
    provided it's at least `low`."""
    sizes = [f for f in _FIBONACCI_CANDIDATES if low <= f <= high and f <= max_n]
    if max_n >= low and max_n not in sizes:
        sizes.append(max_n)
    return sorted(set(sizes))


def golden_ratio_convergence_table() -> list[dict]:
    """Consecutive Fibonacci ratios, showing convergence toward phi —
    the actual mathematical basis for using Fibonacci window sizes."""
    rows = []
    for a, b in zip(_FIBONACCI_CANDIDATES, _FIBONACCI_CANDIDATES[1:]):
        rows.append({"a": a, "b": b, "ratio": b / a, "diff_from_phi": abs(b / a - PHI)})
    return rows


def window_sensitivity_analysis(df: pd.DataFrame, column: str = "two_digit", digits: int = 2, alpha: float = 0.05) -> list[dict]:
    """Runs chi-square + entropy on the LAST n draws, for each Fibonacci
    window size n available given the dataset's length. Lets you see
    whether the randomness verdict is stable across sample sizes, rather
    than relying on a single window."""
    sizes = fibonacci_window_sizes(len(df))
    rows = []
    for n in sizes:
        window = df.tail(n)
        counts = group_frequency(window, column, digits)
        result = _chi_square_from_counts(f"{column} last {n}", counts, alpha)
        entropy, max_entropy, ratio = shannon_entropy_ratio(window, column, digits)
        rows.append({
            "n": n,
            "chi2": result.statistic,
            "p": result.p_value,
            "significant": result.significant,
            "low_n_warning": result.low_expected_count_warning,
            "entropy_ratio": ratio,
        })
    return rows
