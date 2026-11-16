# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=892, k=5, hits=43/892 (4.82%), expected under fairness=5.00%, 95% CI=(3.51%, 6.44%), ROI=-13.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=892, k=5, hits=44/892 (4.93%), expected under fairness=5.00%, 95% CI=(3.61%, 6.57%), ROI=-11.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=892, k=5, hits=47/892 (5.27%), expected under fairness=5.00%, 95% CI=(3.90%, 6.95%), ROI=-5.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=892, k=5, hits=45/892 (5.04%), expected under fairness=5.00%, 95% CI=(3.70%, 6.69%), ROI=-9.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=892, k=5, hits=49/892 (5.49%), expected under fairness=5.00%, 95% CI=(4.09%, 7.20%), ROI=-1.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=892, k=5, hits=3/892 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=892, k=5, hits=4/892 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.14%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=892, k=5, hits=3/892 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=892, k=5, hits=6/892 (0.67%), expected under fairness=0.50%, 95% CI=(0.25%, 1.46%), ROI=-87.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=892, k=5, hits=0/892 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.