"""
dashboard.py
------------
Aggregates all analysis results into a single JSON-serializable dict, then
renders it into a self-contained HTML dashboard (dashboard_template.html
with the data embedded inline — works identically as a local file, a
Claude artifact preview, or a GitHub Pages site, since nothing is fetched
from outside the page itself except the charting library CDN + fonts).
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from . import stats_analysis as sa
from .backtest import BacktestResult

TEMPLATE_PATH = Path(__file__).parent.parent / "dashboard_template.html"
DATA_PLACEHOLDER = "/*__DASHBOARD_DATA_JSON__*/"


def _digit_position_block(df: pd.DataFrame, alpha: float) -> list[dict]:
    blocks = []
    for pos in range(4):
        freq = sa.digit_position_frequency(df, pos)
        result = sa.chi_square_digit_position(df, pos, alpha=alpha)
        blocks.append({
            "position": pos,
            "freq": freq.values.tolist(),
            "chi2": result.statistic,
            "p": result.p_value,
            "significant": result.significant,
        })
    return blocks


def _joint_block(df: pd.DataFrame, column: str, digits: int, alpha: float) -> dict:
    if digits == 2:
        freq = sa.two_digit_frequency(df, column)
        result = sa.chi_square_two_digit(df, column, alpha=alpha)
    else:
        freq = sa.three_digit_frequency(df, column)
        result = sa.chi_square_three_digit(df, column, alpha=alpha)
    return {
        "column": column,
        "digits": digits,
        "freq": freq.values.tolist(),
        "chi2": result.statistic,
        "p": result.p_value,
        "significant": result.significant,
        "low_n_warning": result.low_expected_count_warning,
    }


def _runs_and_autocorr_block(df: pd.DataFrame, column: str) -> dict:
    z_oe, p_oe = sa.odd_even_runs_test(df, column)
    z_med, p_med = sa.above_below_median_runs_test(df, column)
    ac = sa.autocorrelation(df, column, nlags=10)
    return {
        "column": column,
        "odd_even": {"z": z_oe, "p": p_oe},
        "median": {"z": z_med, "p": p_med},
        "acf": [float(v) for v in ac],
    }


def _backtest_block(results: list[BacktestResult]) -> list[dict]:
    return [
        {
            "strategy": r.strategy_name,
            "target": r.target_column,
            "n": r.n_draws,
            "k": r.k_numbers,
            "hits": r.hits,
            "hit_rate": r.hit_rate,
            "expected": r.expected_hit_rate,
            "ci_low": r.ci_low,
            "ci_high": r.ci_high,
            "roi_pct": r.roi_pct,
            "significant": r.beats_baseline_significantly(),
            "cumulative_bankroll": r.cumulative_bankroll,
        }
        for r in results
    ]


def build_dashboard_data(
    df: pd.DataFrame,
    backtest_results_by_target: dict[str, list[BacktestResult]],
    alpha: float = 0.05,
    is_synthetic: bool = False,
) -> dict:
    data = {
        "meta": {
            "n_draws": len(df),
            "date_start": str(df["draw_date"].min().date()),
            "date_end": str(df["draw_date"].max().date()),
            "alpha": alpha,
            "is_synthetic": is_synthetic,
        },
        "digit_positions": _digit_position_block(df, alpha),
        "joint": {
            "two_digit_bottom": _joint_block(df, "two_digit_bottom", 2, alpha),
            "two_digit_top": _joint_block(df, "two_digit_top", 2, alpha),
            "three_digit_top": _joint_block(df, "three_digit_top", 3, alpha),
        },
        "runs_autocorr": {
            "two_digit_bottom": _runs_and_autocorr_block(df, "two_digit_bottom"),
            "two_digit_top": _runs_and_autocorr_block(df, "two_digit_top"),
        },
        "backtest": {
            target: _backtest_block(results)
            for target, results in backtest_results_by_target.items()
        },
    }
    return data


def render_dashboard(data: dict, out_path: str) -> None:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if DATA_PLACEHOLDER not in template:
        raise ValueError(f"Template is missing the {DATA_PLACEHOLDER} placeholder")
    payload = json.dumps(data)
    html = template.replace(DATA_PLACEHOLDER, payload)
    Path(out_path).write_text(html, encoding="utf-8")
