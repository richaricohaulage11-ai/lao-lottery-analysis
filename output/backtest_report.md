# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=869, k=5, hits=55/869 (6.33%), expected under fairness=5.00%, 95% CI=(4.80%, 8.16%), ROI=+13.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=869, k=5, hits=43/869 (4.95%), expected under fairness=5.00%, 95% CI=(3.60%, 6.61%), ROI=-10.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=869, k=5, hits=45/869 (5.18%), expected under fairness=5.00%, 95% CI=(3.80%, 6.87%), ROI=-6.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=869, k=5, hits=45/869 (5.18%), expected under fairness=5.00%, 95% CI=(3.80%, 6.87%), ROI=-6.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=869, k=5, hits=47/869 (5.41%), expected under fairness=5.00%, 95% CI=(4.00%, 7.13%), ROI=-2.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=869, k=5, hits=10/869 (1.15%), expected under fairness=0.50%, 95% CI=(0.55%, 2.11%), ROI=-79.3% -> statistically distinguishable from the random baseline
- [hot_numbers on three_digit] draws=869, k=5, hits=4/869 (0.46%), expected under fairness=0.50%, 95% CI=(0.13%, 1.17%), ROI=-91.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=869, k=5, hits=3/869 (0.35%), expected under fairness=0.50%, 95% CI=(0.07%, 1.01%), ROI=-93.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=869, k=5, hits=6/869 (0.69%), expected under fairness=0.50%, 95% CI=(0.25%, 1.50%), ROI=-87.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=869, k=5, hits=0/869 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.42%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.