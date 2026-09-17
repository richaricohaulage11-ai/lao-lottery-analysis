"""
report.py
---------
Static PNG chart generation (used for the markdown reports; the interactive
web dashboard in dashboard.py/dashboard_template.html is the primary
deliverable for browsing results).
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from .stats_analysis import digit_position_frequency, two_digit_frequency
from .backtest import BacktestResult


def plot_frequency_charts(df: pd.DataFrame, out_path: str) -> None:
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))

    pos0 = digit_position_frequency(df, 0)
    axes[0].bar(pos0.index.astype(str), pos0.values, color="#4C72B0")
    axes[0].axhline(pos0.values.mean(), color="black", linestyle="--", linewidth=1)
    axes[0].set_title("Digit frequency — four_digit position 0 (leftmost)")
    axes[0].set_xlabel("Digit")
    axes[0].set_ylabel("Count")

    pos3 = digit_position_frequency(df, 3)
    axes[1].bar(pos3.index.astype(str), pos3.values, color="#55A868")
    axes[1].axhline(pos3.values.mean(), color="black", linestyle="--", linewidth=1)
    axes[1].set_title("Digit frequency — four_digit position 3 (rightmost)")
    axes[1].set_xlabel("Digit")
    axes[1].set_ylabel("Count")

    tb = two_digit_frequency(df, "two_digit_bottom")
    axes[2].bar(range(100), tb.values, color="#C44E52", width=1.0)
    axes[2].axhline(tb.values.mean(), color="black", linestyle="--", linewidth=1)
    axes[2].set_title("two_digit_bottom frequency (00-99, leading 2 digits)")
    axes[2].set_xlabel("Number (00-99)")
    axes[2].set_ylabel("Count")

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_backtest_curves(results: list[BacktestResult], out_path: str) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    target = results[0].target_column if results else ""
    for r in results:
        ax.plot(r.cumulative_bankroll, label=r.strategy_name)
    ax.axhline(0, color="black", linewidth=1)
    ax.set_title(f"Cumulative bankroll by strategy (walk-forward backtest on {target})")
    ax.set_xlabel("Draw number (since warm-up)")
    ax.set_ylabel("Cumulative profit/loss (bet units)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
