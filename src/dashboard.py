"""
dashboard.py
------------
Aggregates all analysis results into a single JSON-serializable dict, then
renders it into a self-contained HTML dashboard (dashboard_template.html
with the data embedded inline — works identically as a local file, a
Claude artifact preview, or a GitHub Pages site).
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
    freq = sa.group_frequency(df, column, digits)
    result = sa.chi_square_group(df, column, digits, alpha=alpha)
    return {
        "column": column,
        "digits": digits,
        "freq": freq.values.tolist(),
        "chi2": result.statistic,
        "p": result.p_value,
        "significant": result.significant,
        "low_n_warning": result.low_expected_count_warning,
    }


def _runs_and_autocorr_block(df: pd.DataFrame, column: str) -> dict | None:
    if len(df) < 15:
        return None
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


def _extended_block(df: pd.DataFrame, alpha: float) -> dict:
    ks_results = []
    for column, digits in [("two_digit", 2), ("three_digit", 3), ("four_digit", 4)]:
        r = sa.ks_test_uniform(df, column, digits, alpha=alpha)
        ks_results.append({
            "column": column, "statistic": r.statistic, "p": r.p_value, "significant": r.significant,
        })

    entropy_results = []
    for column, digits in [("two_digit", 2), ("three_digit", 3)]:
        entropy, max_entropy, ratio = sa.shannon_entropy_ratio(df, column, digits)
        entropy_results.append({
            "column": column, "entropy": entropy, "max_entropy": max_entropy, "ratio": ratio,
        })

    homogeneity = {}
    for group_by in ["month", "year", "weekday"]:
        rows = []
        for pos in range(4):
            r = sa.chi_square_homogeneity(df, pos, group_by, alpha=alpha)
            if r is not None:
                rows.append({
                    "position": pos, "statistic": r.statistic, "p": r.p_value,
                    "dof": r.dof, "n_groups": r.n_groups, "significant": r.significant,
                    "low_n_warning": r.low_expected_count_warning,
                })
        homogeneity[group_by] = rows

    monthly = {
        "two_digit": sa.monthly_series(df, "two_digit"),
        "three_digit": sa.monthly_series(df, "three_digit"),
    }

    return {
        "ks_tests": ks_results,
        "entropy": entropy_results,
        "homogeneity": homogeneity,
        "monthly_trend": monthly,
        "window_sensitivity": sa.window_sensitivity_analysis(df, "two_digit", 2, alpha),
        "golden_ratio_convergence": sa.golden_ratio_convergence_table(),
    }


def _summary_block(df: pd.DataFrame, digit_positions: list[dict], joint: dict, backtest_by_target: dict) -> dict:
    """Plain-language summary verdict, computed once here so the
    dashboard's top banner doesn't need to re-derive logic in JS."""
    n_draws = len(df)
    sig_marginal = sum(1 for d in digit_positions if d["significant"])
    sig_joint = sum(1 for j in joint.values() if j["significant"])
    total_random_tests = len(digit_positions) + len(joint)
    total_sig = sig_marginal + sig_joint

    any_strategy_beats = False
    for results in backtest_by_target.values():
        for r in results:
            if r.beats_baseline_significantly() and r.strategy_name != "random_baseline":
                any_strategy_beats = True

    has_backtest = len(backtest_by_target) > 0

    if total_random_tests > 0:
        randomness_verdict = (
            "สอดคล้องกับการสุ่มที่ยุติธรรม"
            if total_sig <= max(1, round(total_random_tests * 0.05 + 0.5))
            else "มีบางจุดเบี่ยงเบนที่ควรตรวจสอบเพิ่มเติม"
        )
    else:
        randomness_verdict = "ยังไม่มีข้อมูลพอจะสรุป"

    if not has_backtest:
        backtest_verdict = "ยังไม่มีข้อมูลพอสำหรับ backtest"
    elif any_strategy_beats:
        backtest_verdict = "พบกลยุทธ์ที่ชนะการสุ่มอย่างมีนัยสำคัญ (ควรตรวจสอบซ้ำ — อาจเป็น multiple testing)"
    else:
        backtest_verdict = "ไม่มีกลยุทธ์ใดเอาชนะการสุ่มได้อย่างมีนัยสำคัญ (รวมกลยุทธ์อิงสัดส่วนทองคำ)"

    return {
        "n_draws": n_draws,
        "sig_count": total_sig,
        "total_tests": total_random_tests,
        "randomness_verdict": randomness_verdict,
        "backtest_verdict": backtest_verdict,
        "has_backtest": has_backtest,
    }


def build_dashboard_data(
    df: pd.DataFrame,
    backtest_results_by_target: dict[str, list[BacktestResult]],
    alpha: float = 0.05,
    is_synthetic: bool = False,
) -> dict:
    digit_positions = _digit_position_block(df, alpha)
    joint = {
        "two_digit": _joint_block(df, "two_digit", 2, alpha),
        "three_digit": _joint_block(df, "three_digit", 3, alpha),
        "four_digit": _joint_block(df, "four_digit", 4, alpha),
    }
    return {
        "meta": {
            "n_draws": len(df),
            "date_start": str(df["draw_date"].min().date()),
            "date_end": str(df["draw_date"].max().date()),
            "alpha": alpha,
            "is_synthetic": is_synthetic,
        },
        "summary": _summary_block(df, digit_positions, joint, backtest_results_by_target),
        "digit_positions": digit_positions,
        "joint": joint,
        "runs_autocorr": {
            "two_digit": _runs_and_autocorr_block(df, "two_digit"),
            "three_digit": _runs_and_autocorr_block(df, "three_digit"),
        },
        "extended": _extended_block(df, alpha),
        "backtest": {
            target: _backtest_block(results)
            for target, results in backtest_results_by_target.items()
        },
    }


def render_dashboard(data: dict, out_path: str) -> None:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if DATA_PLACEHOLDER not in template:
        raise ValueError(f"Template is missing the {DATA_PLACEHOLDER} placeholder")
    payload = json.dumps(data)
    # Defensive: escape any literal "</script>" so it can never prematurely
    # close the <script type="application/json"> tag it's embedded in.
    payload = payload.replace("</script", "<\\/script")
    html = template.replace(DATA_PLACEHOLDER, payload)
    Path(out_path).write_text(html, encoding="utf-8")
