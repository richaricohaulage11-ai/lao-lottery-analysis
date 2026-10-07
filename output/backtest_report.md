# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=875, k=5, hits=37/875 (4.23%), expected under fairness=5.00%, 95% CI=(2.99%, 5.78%), ROI=-23.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=875, k=5, hits=44/875 (5.03%), expected under fairness=5.00%, 95% CI=(3.68%, 6.69%), ROI=-9.5% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=875, k=5, hits=45/875 (5.14%), expected under fairness=5.00%, 95% CI=(3.78%, 6.82%), ROI=-7.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=875, k=5, hits=45/875 (5.14%), expected under fairness=5.00%, 95% CI=(3.78%, 6.82%), ROI=-7.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=875, k=5, hits=48/875 (5.49%), expected under fairness=5.00%, 95% CI=(4.07%, 7.21%), ROI=-1.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=875, k=5, hits=4/875 (0.46%), expected under fairness=0.50%, 95% CI=(0.12%, 1.17%), ROI=-91.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=875, k=5, hits=4/875 (0.46%), expected under fairness=0.50%, 95% CI=(0.12%, 1.17%), ROI=-91.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=875, k=5, hits=3/875 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 1.00%), ROI=-93.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=875, k=5, hits=6/875 (0.69%), expected under fairness=0.50%, 95% CI=(0.25%, 1.49%), ROI=-87.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=875, k=5, hits=0/875 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.