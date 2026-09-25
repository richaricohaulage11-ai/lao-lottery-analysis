# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=870, k=5, hits=41/870 (4.71%), expected under fairness=5.00%, 95% CI=(3.40%, 6.34%), ROI=-15.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=870, k=5, hits=43/870 (4.94%), expected under fairness=5.00%, 95% CI=(3.60%, 6.60%), ROI=-11.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=870, k=5, hits=45/870 (5.17%), expected under fairness=5.00%, 95% CI=(3.80%, 6.86%), ROI=-6.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=870, k=5, hits=45/870 (5.17%), expected under fairness=5.00%, 95% CI=(3.80%, 6.86%), ROI=-6.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=870, k=5, hits=47/870 (5.40%), expected under fairness=5.00%, 95% CI=(4.00%, 7.12%), ROI=-2.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=870, k=5, hits=6/870 (0.69%), expected under fairness=0.50%, 95% CI=(0.25%, 1.50%), ROI=-87.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=870, k=5, hits=4/870 (0.46%), expected under fairness=0.50%, 95% CI=(0.13%, 1.17%), ROI=-91.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=870, k=5, hits=3/870 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 1.00%), ROI=-93.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=870, k=5, hits=6/870 (0.69%), expected under fairness=0.50%, 95% CI=(0.25%, 1.50%), ROI=-87.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=870, k=5, hits=0/870 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.