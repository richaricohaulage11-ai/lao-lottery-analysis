# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit_bottom
- [random_baseline on two_digit_bottom] draws=370, k=5, hits=19/370 (5.14%), expected under fairness=5.00%, 95% CI=(3.12%, 7.90%), ROI=-7.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit_bottom] draws=370, k=5, hits=18/370 (4.86%), expected under fairness=5.00%, 95% CI=(2.91%, 7.58%), ROI=-12.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit_bottom] draws=370, k=5, hits=18/370 (4.86%), expected under fairness=5.00%, 95% CI=(2.91%, 7.58%), ROI=-12.4% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit_bottom] draws=370, k=5, hits=20/370 (5.41%), expected under fairness=5.00%, 95% CI=(3.33%, 8.22%), ROI=-2.7% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: two_digit_top
- [random_baseline on two_digit_top] draws=370, k=5, hits=19/370 (5.14%), expected under fairness=5.00%, 95% CI=(3.12%, 7.90%), ROI=-7.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit_top] draws=370, k=5, hits=22/370 (5.95%), expected under fairness=5.00%, 95% CI=(3.76%, 8.86%), ROI=+7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit_top] draws=370, k=5, hits=22/370 (5.95%), expected under fairness=5.00%, 95% CI=(3.76%, 8.86%), ROI=+7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit_top] draws=370, k=5, hits=22/370 (5.95%), expected under fairness=5.00%, 95% CI=(3.76%, 8.86%), ROI=+7.0% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Verdict
No strategy showed a statistically significant edge over the fair-game expectation, on any target category. This is the result predicted by probability theory for a fair lottery, and matches findings in the peer-reviewed literature on other lotteries (see the companion research report).