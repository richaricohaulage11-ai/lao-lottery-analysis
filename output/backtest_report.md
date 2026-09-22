# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=384, k=5, hits=22/384 (5.73%), expected under fairness=5.00%, 95% CI=(3.62%, 8.55%), ROI=+3.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=384, k=5, hits=17/384 (4.43%), expected under fairness=5.00%, 95% CI=(2.60%, 6.99%), ROI=-20.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=384, k=5, hits=18/384 (4.69%), expected under fairness=5.00%, 95% CI=(2.80%, 7.31%), ROI=-15.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=384, k=5, hits=20/384 (5.21%), expected under fairness=5.00%, 95% CI=(3.21%, 7.93%), ROI=-6.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=384, k=5, hits=13/384 (3.39%), expected under fairness=5.00%, 95% CI=(1.81%, 5.72%), ROI=-39.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=384, k=5, hits=2/384 (0.52%), expected under fairness=0.50%, 95% CI=(0.06%, 1.87%), ROI=-90.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=384, k=5, hits=2/384 (0.52%), expected under fairness=0.50%, 95% CI=(0.06%, 1.87%), ROI=-90.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=384, k=5, hits=1/384 (0.26%), expected under fairness=0.50%, 95% CI=(0.01%, 1.44%), ROI=-95.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=384, k=5, hits=1/384 (0.26%), expected under fairness=0.50%, 95% CI=(0.01%, 1.44%), ROI=-95.3% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=384, k=5, hits=2/384 (0.52%), expected under fairness=0.50%, 95% CI=(0.06%, 1.87%), ROI=-90.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Verdict
No strategy showed a statistically significant edge over the fair-game expectation, on any target category. This is the result predicted by probability theory for a fair lottery, and matches findings in the peer-reviewed literature on other lotteries (see the companion research report).