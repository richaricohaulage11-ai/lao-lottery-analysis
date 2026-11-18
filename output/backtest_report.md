# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=893, k=5, hits=43/893 (4.82%), expected under fairness=5.00%, 95% CI=(3.51%, 6.43%), ROI=-13.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=893, k=5, hits=44/893 (4.93%), expected under fairness=5.00%, 95% CI=(3.60%, 6.56%), ROI=-11.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=893, k=5, hits=47/893 (5.26%), expected under fairness=5.00%, 95% CI=(3.89%, 6.94%), ROI=-5.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=893, k=5, hits=45/893 (5.04%), expected under fairness=5.00%, 95% CI=(3.70%, 6.69%), ROI=-9.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=893, k=5, hits=49/893 (5.49%), expected under fairness=5.00%, 95% CI=(4.09%, 7.19%), ROI=-1.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=893, k=5, hits=3/893 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-94.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=893, k=5, hits=4/893 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.14%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=893, k=5, hits=3/893 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-94.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=893, k=5, hits=6/893 (0.67%), expected under fairness=0.50%, 95% CI=(0.25%, 1.46%), ROI=-87.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=893, k=5, hits=0/893 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.