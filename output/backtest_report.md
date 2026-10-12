# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=877, k=5, hits=53/877 (6.04%), expected under fairness=5.00%, 95% CI=(4.56%, 7.83%), ROI=+8.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=877, k=5, hits=44/877 (5.02%), expected under fairness=5.00%, 95% CI=(3.67%, 6.68%), ROI=-9.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=877, k=5, hits=45/877 (5.13%), expected under fairness=5.00%, 95% CI=(3.77%, 6.81%), ROI=-7.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=877, k=5, hits=45/877 (5.13%), expected under fairness=5.00%, 95% CI=(3.77%, 6.81%), ROI=-7.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=877, k=5, hits=48/877 (5.47%), expected under fairness=5.00%, 95% CI=(4.06%, 7.19%), ROI=-1.5% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=877, k=5, hits=5/877 (0.57%), expected under fairness=0.50%, 95% CI=(0.19%, 1.33%), ROI=-89.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=877, k=5, hits=4/877 (0.46%), expected under fairness=0.50%, 95% CI=(0.12%, 1.16%), ROI=-91.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=877, k=5, hits=3/877 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 1.00%), ROI=-93.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=877, k=5, hits=6/877 (0.68%), expected under fairness=0.50%, 95% CI=(0.25%, 1.48%), ROI=-87.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=877, k=5, hits=0/877 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.