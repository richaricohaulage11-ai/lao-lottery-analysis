# Randomness Test Report

Draws analyzed: 4
Date range: 2026-09-14 to 2026-09-21

Reminder: every prize category below (5/4/3/2 ตัว) is a trailing slice of the SAME 4-digit draw (four_digit), not a separate random draw. See data_loader.py for exactly which digits map to which category.

## Part 1: Marginal chi-square, per digit position of four_digit
- four_digit position 0 (marginal): chi2=11.000, p=0.2757, n=4, categories=10 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- four_digit position 1 (marginal): chi2=6.000, p=0.7399, n=4, categories=10 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- four_digit position 2 (marginal): chi2=11.000, p=0.2757, n=4, categories=10 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- four_digit position 3 (marginal): chi2=11.000, p=0.2757, n=4, categories=10 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]

## Part 2: Joint/interaction chi-square on the derived prize categories
- two_digit (2 digits, joint/interaction test): chi2=146.000, p=0.0015, n=4, categories=100 -> significant deviation from uniform (p < 0.05) [LOW SAMPLE WARNING: expected count per category < 5]
- three_digit (3 digits, joint/interaction test): chi2=996.000, p=0.5208, n=4, categories=1000 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- four_digit (4 digits, joint/interaction test): chi2=9996.000, p=0.5066, n=4, categories=10000 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]

## Runs tests
- Skipped: only 4 draw(s) loaded, need at least 10 for a meaningful runs test. Will populate automatically as more real draws are collected.

## Autocorrelation (lags 1-10)
- Skipped: only 4 draw(s) loaded, need at least 15 for a 10-lag autocorrelation. Will populate automatically as more real draws are collected.

## Interpretation
1 of 7 chi-square tests were significant at alpha=0.05. With 7 tests at alpha=0.05, roughly 0.4 false positives are expected by chance alone — a single isolated significant result is not strong evidence of bias. A consistent pattern across positions, prize categories, and separate time windows would be needed before concluding the draw is not fair.
None of this measures predictability. A perfectly fair process can still show one 'significant' test out of several by chance — that is the expected multiple-testing effect, not a flaw.