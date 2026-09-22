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
