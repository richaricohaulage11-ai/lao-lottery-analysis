# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=370, k=5, hits=14/370 (3.78%), expected under fairness=5.00%, 95% CI=(2.08%, 6.27%), ROI=-31.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=370, k=5, hits=22/370 (5.95%), expected under fairness=5.00%, 95% CI=(3.76%, 8.86%), ROI=+7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=370, k=5, hits=22/370 (5.95%), expected under fairness=5.00%, 95% CI=(3.76%, 8.86%), ROI=+7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=370, k=5, hits=22/370 (5.95%), expected under fairness=5.00%, 95% CI=(3.76%, 8.86%), ROI=+7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=370, k=5, hits=22/370 (5.95%), expected under fairness=5.00%, 95% CI=(3.76%, 8.86%), ROI=+7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=370, k=5, hits=4/370 (1.08%), expected under fairness=0.50%, 95% CI=(0.30%, 2.74%), ROI=-80.5% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=370, k=5, hits=3/370 (0.81%), expected under fairness=0.50%, 95% CI=(0.17%, 2.35%), ROI=-85.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=370, k=5, hits=1/370 (0.27%), expected under fairness=0.50%, 95% CI=(0.01%, 1.50%), ROI=-95.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=370, k=5, hits=2/370 (0.54%), expected under fairness=0.50%, 95% CI=(0.07%, 1.94%), ROI=-90.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=370, k=5, hits=0/370 (0.00%), expected under fairness=0.50%, 95% CI=(0.00%, 0.99%), ROI=-100.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Verdict
No strategy showed a statistically significant edge over the fair-game expectation, on any target category. This is the result predicted by probability theory for a fair lottery, and matches findings in the peer-reviewed literature on other lotteries (see the companion research report).