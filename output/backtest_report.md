# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=888, k=5, hits=56/888 (6.31%), expected under fairness=5.00%, 95% CI=(4.80%, 8.11%), ROI=+13.5% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=888, k=5, hits=44/888 (4.95%), expected under fairness=5.00%, 95% CI=(3.62%, 6.60%), ROI=-10.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=888, k=5, hits=46/888 (5.18%), expected under fairness=5.00%, 95% CI=(3.82%, 6.85%), ROI=-6.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=888, k=5, hits=45/888 (5.07%), expected under fairness=5.00%, 95% CI=(3.72%, 6.72%), ROI=-8.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=888, k=5, hits=49/888 (5.52%), expected under fairness=5.00%, 95% CI=(4.11%, 7.23%), ROI=-0.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=888, k=5, hits=7/888 (0.79%), expected under fairness=0.50%, 95% CI=(0.32%, 1.62%), ROI=-85.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=888, k=5, hits=4/888 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.15%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=888, k=5, hits=3/888 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=888, k=5, hits=6/888 (0.68%), expected under fairness=0.50%, 95% CI=(0.25%, 1.46%), ROI=-87.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=888, k=5, hits=0/888 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.