# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=890, k=5, hits=54/890 (6.07%), expected under fairness=5.00%, 95% CI=(4.59%, 7.84%), ROI=+9.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=890, k=5, hits=44/890 (4.94%), expected under fairness=5.00%, 95% CI=(3.61%, 6.58%), ROI=-11.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=890, k=5, hits=46/890 (5.17%), expected under fairness=5.00%, 95% CI=(3.81%, 6.83%), ROI=-7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=890, k=5, hits=45/890 (5.06%), expected under fairness=5.00%, 95% CI=(3.71%, 6.71%), ROI=-9.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=890, k=5, hits=49/890 (5.51%), expected under fairness=5.00%, 95% CI=(4.10%, 7.21%), ROI=-0.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=890, k=5, hits=5/890 (0.56%), expected under fairness=0.50%, 95% CI=(0.18%, 1.31%), ROI=-89.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=890, k=5, hits=4/890 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.15%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=890, k=5, hits=3/890 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=890, k=5, hits=6/890 (0.67%), expected under fairness=0.50%, 95% CI=(0.25%, 1.46%), ROI=-87.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=890, k=5, hits=0/890 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.