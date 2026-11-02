# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=886, k=5, hits=50/886 (5.64%), expected under fairness=5.00%, 95% CI=(4.22%, 7.37%), ROI=+1.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=886, k=5, hits=44/886 (4.97%), expected under fairness=5.00%, 95% CI=(3.63%, 6.61%), ROI=-10.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=886, k=5, hits=46/886 (5.19%), expected under fairness=5.00%, 95% CI=(3.83%, 6.86%), ROI=-6.5% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=886, k=5, hits=45/886 (5.08%), expected under fairness=5.00%, 95% CI=(3.73%, 6.74%), ROI=-8.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=886, k=5, hits=49/886 (5.53%), expected under fairness=5.00%, 95% CI=(4.12%, 7.25%), ROI=-0.5% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=886, k=5, hits=7/886 (0.79%), expected under fairness=0.50%, 95% CI=(0.32%, 1.62%), ROI=-85.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=886, k=5, hits=4/886 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.15%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=886, k=5, hits=3/886 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.99%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=886, k=5, hits=6/886 (0.68%), expected under fairness=0.50%, 95% CI=(0.25%, 1.47%), ROI=-87.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=886, k=5, hits=0/886 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.