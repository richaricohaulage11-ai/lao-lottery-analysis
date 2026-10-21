# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=881, k=5, hits=39/881 (4.43%), expected under fairness=5.00%, 95% CI=(3.17%, 6.00%), ROI=-20.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=881, k=5, hits=44/881 (4.99%), expected under fairness=5.00%, 95% CI=(3.65%, 6.65%), ROI=-10.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=881, k=5, hits=45/881 (5.11%), expected under fairness=5.00%, 95% CI=(3.75%, 6.78%), ROI=-8.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=881, k=5, hits=45/881 (5.11%), expected under fairness=5.00%, 95% CI=(3.75%, 6.78%), ROI=-8.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=881, k=5, hits=48/881 (5.45%), expected under fairness=5.00%, 95% CI=(4.04%, 7.16%), ROI=-1.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=881, k=5, hits=4/881 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.16%), ROI=-91.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=881, k=5, hits=4/881 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.16%), ROI=-91.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=881, k=5, hits=3/881 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.99%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=881, k=5, hits=6/881 (0.68%), expected under fairness=0.50%, 95% CI=(0.25%, 1.48%), ROI=-87.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=881, k=5, hits=0/881 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.