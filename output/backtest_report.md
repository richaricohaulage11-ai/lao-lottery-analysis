# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=887, k=5, hits=40/887 (4.51%), expected under fairness=5.00%, 95% CI=(3.24%, 6.09%), ROI=-18.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=887, k=5, hits=44/887 (4.96%), expected under fairness=5.00%, 95% CI=(3.63%, 6.60%), ROI=-10.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=887, k=5, hits=46/887 (5.19%), expected under fairness=5.00%, 95% CI=(3.82%, 6.86%), ROI=-6.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=887, k=5, hits=45/887 (5.07%), expected under fairness=5.00%, 95% CI=(3.72%, 6.73%), ROI=-8.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=887, k=5, hits=49/887 (5.52%), expected under fairness=5.00%, 95% CI=(4.11%, 7.24%), ROI=-0.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=887, k=5, hits=4/887 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.15%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=887, k=5, hits=4/887 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.15%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=887, k=5, hits=3/887 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.99%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=887, k=5, hits=6/887 (0.68%), expected under fairness=0.50%, 95% CI=(0.25%, 1.47%), ROI=-87.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=887, k=5, hits=0/887 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.