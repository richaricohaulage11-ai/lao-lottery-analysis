# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=896, k=5, hits=45/896 (5.02%), expected under fairness=5.00%, 95% CI=(3.69%, 6.66%), ROI=-9.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=896, k=5, hits=44/896 (4.91%), expected under fairness=5.00%, 95% CI=(3.59%, 6.54%), ROI=-11.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=896, k=5, hits=47/896 (5.25%), expected under fairness=5.00%, 95% CI=(3.88%, 6.91%), ROI=-5.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=896, k=5, hits=45/896 (5.02%), expected under fairness=5.00%, 95% CI=(3.69%, 6.66%), ROI=-9.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=896, k=5, hits=50/896 (5.58%), expected under fairness=5.00%, 95% CI=(4.17%, 7.29%), ROI=+0.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=896, k=5, hits=7/896 (0.78%), expected under fairness=0.50%, 95% CI=(0.31%, 1.60%), ROI=-85.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=896, k=5, hits=4/896 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.14%), ROI=-92.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=896, k=5, hits=3/896 (0.33%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-94.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=896, k=5, hits=6/896 (0.67%), expected under fairness=0.50%, 95% CI=(0.25%, 1.45%), ROI=-87.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=896, k=5, hits=0/896 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.