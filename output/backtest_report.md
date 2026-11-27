# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=897, k=5, hits=55/897 (6.13%), expected under fairness=5.00%, 95% CI=(4.65%, 7.91%), ROI=+10.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=897, k=5, hits=44/897 (4.91%), expected under fairness=5.00%, 95% CI=(3.59%, 6.53%), ROI=-11.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=897, k=5, hits=48/897 (5.35%), expected under fairness=5.00%, 95% CI=(3.97%, 7.03%), ROI=-3.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=897, k=5, hits=45/897 (5.02%), expected under fairness=5.00%, 95% CI=(3.68%, 6.66%), ROI=-9.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=897, k=5, hits=50/897 (5.57%), expected under fairness=5.00%, 95% CI=(4.17%, 7.28%), ROI=+0.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=897, k=5, hits=4/897 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.14%), ROI=-92.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=897, k=5, hits=4/897 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.14%), ROI=-92.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=897, k=5, hits=3/897 (0.33%), expected under fairness=0.50%, 95% CI=(0.07%, 0.97%), ROI=-94.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=897, k=5, hits=6/897 (0.67%), expected under fairness=0.50%, 95% CI=(0.25%, 1.45%), ROI=-88.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=897, k=5, hits=0/897 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.