# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=894, k=5, hits=57/894 (6.38%), expected under fairness=5.00%, 95% CI=(4.86%, 8.18%), ROI=+14.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=894, k=5, hits=44/894 (4.92%), expected under fairness=5.00%, 95% CI=(3.60%, 6.55%), ROI=-11.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=894, k=5, hits=47/894 (5.26%), expected under fairness=5.00%, 95% CI=(3.89%, 6.93%), ROI=-5.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=894, k=5, hits=45/894 (5.03%), expected under fairness=5.00%, 95% CI=(3.69%, 6.68%), ROI=-9.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=894, k=5, hits=49/894 (5.48%), expected under fairness=5.00%, 95% CI=(4.08%, 7.18%), ROI=-1.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=894, k=5, hits=5/894 (0.56%), expected under fairness=0.50%, 95% CI=(0.18%, 1.30%), ROI=-89.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=894, k=5, hits=4/894 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.14%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=894, k=5, hits=3/894 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-94.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=894, k=5, hits=6/894 (0.67%), expected under fairness=0.50%, 95% CI=(0.25%, 1.46%), ROI=-87.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=894, k=5, hits=0/894 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.