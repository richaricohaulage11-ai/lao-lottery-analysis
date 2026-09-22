"""
main.py
-------
Runs the full pipeline: load data -> randomness tests -> backtest (on both
two_digit and three_digit, once there's enough data) -> charts, markdown
reports, and a self-contained HTML dashboard, all written to output/.

Usage:
    python main.py                          # uses bundled sample data
    python main.py --data path/to/real.csv  # uses your own data
"""
from __future__ import annotations

import argparse
import os

from src.data_loader import load_draws, basic_summary
from src.stats_analysis import full_randomness_report, extended_methods_report
from src.strategies import ALL_STRATEGIES
from src.backtest import compare_strategies, backtest_report
from src.report import plot_frequency_charts, plot_backtest_curves
from src.dashboard import build_dashboard_data, render_dashboard

BACKTEST_TARGETS = ["two_digit", "three_digit"]
MIN_DRAWS_FOR_BACKTEST_BUFFER = 5  # need at least min_history + this many draws to backtest at all


def main():
    parser = argparse.ArgumentParser(description="Lao lottery statistical analysis + backtest")
    parser.add_argument("--data", default="data/sample_draws.csv", help="Path to draws CSV")
    parser.add_argument("--output", default="output", help="Output directory")
    parser.add_argument("--min-history", type=int, default=30, help="Warm-up draws before backtesting starts")
    parser.add_argument("--k", type=int, default=5, help="Numbers bet on per draw, per strategy")
    parser.add_argument("--payout", type=float, default=90.0, help="Payout multiplier for a correct 2-digit bet")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    is_synthetic = args.data.endswith("sample_draws.csv")

    print("Loading data...")
    df = load_draws(args.data)
    print(basic_summary(df))
    print()

    if is_synthetic:
        print(
            "NOTE: running on bundled SYNTHETIC demo data. Replace with real, "
            "cross-checked historical draws before drawing any real conclusions "
            "(see README.md).\n"
        )

    print("Running randomness tests...")
    rand_report = full_randomness_report(df)
    rand_path = os.path.join(args.output, "randomness_report.md")
    with open(rand_path, "w", encoding="utf-8") as f:
        f.write(rand_report)
    print(f"  -> {rand_path}")

    print("Generating frequency charts...")
    freq_chart_path = os.path.join(args.output, "frequency_charts.png")
    plot_frequency_charts(df, freq_chart_path)
    print(f"  -> {freq_chart_path}")

    print("Running extended methods (KS test, entropy, month/year/weekday homogeneity)...")
    ext_report = extended_methods_report(df)
    ext_path = os.path.join(args.output, "extended_report.md")
    with open(ext_path, "w", encoding="utf-8") as f:
        f.write(ext_report)
    print(f"  -> {ext_path}")

    enough_for_backtest = len(df) > args.min_history + MIN_DRAWS_FOR_BACKTEST_BUFFER
    results_by_target: dict[str, list] = {}

    if enough_for_backtest:
        print("Running backtests (walk-forward, no lookahead) on:", ", ".join(BACKTEST_TARGETS))
        for target in BACKTEST_TARGETS:
            strategies = [cls(target_column=target, k=args.k) for cls in ALL_STRATEGIES]
            results_by_target[target] = compare_strategies(
                df, strategies, min_history=args.min_history, payout_multiplier=args.payout
            )

        all_results = [r for results in results_by_target.values() for r in results]
        bt_report = backtest_report(all_results)

        print("Generating backtest curve chart...")
        bt_chart_path = os.path.join(args.output, "backtest_curve.png")
        plot_backtest_curves(results_by_target[BACKTEST_TARGETS[0]], bt_chart_path)
        print(f"  -> {bt_chart_path}")
    else:
        needed = args.min_history + MIN_DRAWS_FOR_BACKTEST_BUFFER
        print(
            f"Skipping backtest: only {len(df)} draw(s) loaded, need > {needed} "
            f"for a meaningful walk-forward backtest. This is expected while a "
            f"real, growing dataset is still small — it will start automatically "
            f"once enough draws have accumulated."
        )
        bt_report = (
            "# Backtest Report\n\n"
            f"Not enough data yet: {len(df)} draw(s) loaded, but a walk-forward "
            f"backtest needs more than {needed} draws to produce a meaningful "
            f"result (it needs `--min-history` warm-up draws before it can even "
            f"start predicting, plus enough draws after that to say anything "
            f"statistically). This section will populate automatically as more "
            f"real draws are collected.\n"
        )

    bt_path = os.path.join(args.output, "backtest_report.md")
    with open(bt_path, "w", encoding="utf-8") as f:
        f.write(bt_report)
    print(f"  -> {bt_path}")

    print("Building web dashboard...")
    dashboard_data = build_dashboard_data(df, results_by_target, is_synthetic=is_synthetic)
    dashboard_path = os.path.join(args.output, "dashboard.html")
    render_dashboard(dashboard_data, dashboard_path)
    print(f"  -> {dashboard_path}")

    print("\nDone. See the output/ directory for full reports, charts, and the dashboard.")


if __name__ == "__main__":
    main()
