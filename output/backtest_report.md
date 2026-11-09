# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=889, k=5, hits=42/889 (4.72%), expected under fairness=5.00%, 95% CI=(3.43%, 6.33%), ROI=-15.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=889, k=5, hits=44/889 (4.95%), expected under fairness=5.00%, 95% CI=(3.62%, 6.59%), ROI=-10.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=889, k=5, hits=46/889 (5.17%), expected under fairness=5.00%, 95% CI=(3.81%, 6.84%), ROI=-6.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=889, k=5, hits=45/889 (5.06%), expected under fairness=5.00%, 95% CI=(3.72%, 6.71%), ROI=-8.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=889, k=5, hits=49/889 (5.51%), expected under fairness=5.00%, 95% CI=(4.11%, 7.22%), ROI=-0.8% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=889, k=5, hits=4/889 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.15%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=889, k=5, hits=4/889 (0.45%), expected under fairness=0.50%, 95% CI=(0.12%, 1.15%), ROI=-91.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=889, k=5, hits=3/889 (0.34%), expected under fairness=0.50%, 95% CI=(0.07%, 0.98%), ROI=-93.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=889, k=5, hits=6/889 (0.67%), expected under fairness=0.50%, 95% CI=(0.25%, 1.46%), ROI=-87.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=889, k=5, hits=0/889 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.41%), ROI=-100.0% -> statistically distinguishable from the random baseline

## Verdict
One or more non-baseline strategies showed a statistically significant deviation from the fair-game expectation in this sample. Given multiple strategies and targets were tested, check whether this survives correction for multiple comparisons and whether it replicates on an independent, later sample before drawing any conclusion — a single significant result among several tests is exactly what chance alone would occasionally produce.