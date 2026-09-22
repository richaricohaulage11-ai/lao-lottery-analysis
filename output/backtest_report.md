# Backtest Report

Every strategy is walk-forward (no lookahead) and compared to the theoretical fair-game expectation and to a random-baseline control. A strategy only has a demonstrated edge if its 95% confidence interval excludes the fair-game expected hit rate.

## Target: two_digit
- [random_baseline on two_digit] draws=729, k=5, hits=33/729 (4.53%), expected under fairness=5.00%, 95% CI=(3.14%, 6.30%), ROI=-18.5% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on two_digit] draws=729, k=5, hits=30/729 (4.12%), expected under fairness=5.00%, 95% CI=(2.79%, 5.82%), ROI=-25.9% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on two_digit] draws=729, k=5, hits=40/729 (5.49%), expected under fairness=5.00%, 95% CI=(3.95%, 7.40%), ROI=-1.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on two_digit] draws=729, k=5, hits=37/729 (5.08%), expected under fairness=5.00%, 95% CI=(3.60%, 6.93%), ROI=-8.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on two_digit] draws=729, k=5, hits=43/729 (5.90%), expected under fairness=5.00%, 95% CI=(4.30%, 7.86%), ROI=+6.2% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Target: three_digit
- [random_baseline on three_digit] draws=729, k=5, hits=4/729 (0.55%), expected under fairness=0.50%, 95% CI=(0.15%, 1.40%), ROI=-90.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [hot_numbers on three_digit] draws=729, k=5, hits=2/729 (0.27%), expected under fairness=0.50%, 95% CI=(0.03%, 0.99%), ROI=-95.1% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [cold_numbers on three_digit] draws=729, k=5, hits=3/729 (0.41%), expected under fairness=0.50%, 95% CI=(0.08%, 1.20%), ROI=-92.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [last_draw_repeat on three_digit] draws=729, k=5, hits=3/729 (0.41%), expected under fairness=0.50%, 95% CI=(0.08%, 1.20%), ROI=-92.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)
- [golden_ratio_sequence on three_digit] draws=729, k=5, hits=3/729 (0.41%), expected under fairness=0.50%, 95% CI=(0.08%, 1.20%), ROI=-92.6% -> NOT statistically distinguishable from the random baseline (consistent with no real edge)

## Verdict
No strategy showed a statistically significant edge over the fair-game expectation, on any target category. This is the result predicted by probability theory for a fair lottery, and matches findings in the peer-reviewed literature on other lotteries (see the companion research report).