# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=873, k=5, hits=42/873 (4.81%), expected under fairness=5.00%, 95% CI=(3.49%, 6.45%), ROI=-13.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=873, k=5, hits=44/873 (5.04%), expected under fairness=5.00%, 95% CI=(3.69%, 6.71%), ROI=-9.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=873, k=5, hits=45/873 (5.15%), expected under fairness=5.00%, 95% CI=(3.78%, 6.84%), ROI=-7.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=873, k=5, hits=45/873 (5.15%), expected under fairness=5.00%, 95% CI=(3.78%, 6.84%), ROI=-7.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=873, k=5, hits=47/873 (5.38%), expected under fairness=5.00%, 95% CI=(3.98%, 7.10%), ROI=-3.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=873, k=5, hits=4/873 (0.46%), expected under fairness=0.50%, 95% CI=(0.12%, 1.17%), ROI=-91.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=873, k=5, hits=4/873 (0.46%), expected under fairness=0.50%, 95% CI=(0.12%, 1.17%), ROI=-91.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=873, k=5, hits=3/873 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 1.00%), ROI=-93.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=873, k=5, hits=6/873 (0.69%), expected under fairness=0.50%, 95% CI=(0.25%, 1.49%), ROI=-87.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=873, k=5, hits=0/873 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.