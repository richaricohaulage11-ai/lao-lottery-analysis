# Randomness Test Report

Draws analyzed: 905
Date range: 2017-10-04 to 2026-10-05

Reminder: every prize category below (5/4/3/2 ตัว) is a trailing slice of the SAME 4-digit draw (four_digit), not a separate random draw. See data_loader.py for exactly which digits map to which category.

## Part 1: Marginal chi-square, per digit position of four_digit
- four_digit position 0 (marginal): chi2=16.138, p=0.0641, n=905, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 1 (marginal): chi2=3.343, p=0.9492, n=905, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 2 (marginal): chi2=5.420, p=0.7963, n=905, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 3 (marginal): chi2=12.249, p=0.1997, n=905, categories=10 -> consistent with uniform (fails to reject randomness)

## Part 2: Joint/interaction chi-square on the derived prize categories
- two_digit (2 digits, joint/interaction test): chi2=105.718, p=0.3036, n=905, categories=100 -> consistent with uniform (fails to reject randomness)
- three_digit (3 digits, joint/interaction test): chi2=1020.967, p=0.3076, n=905, categories=1000 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- four_digit (4 digits, joint/interaction test): chi2=10155.773, p=0.1340, n=905, categories=10000 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]

## Runs tests
- two_digit odd/even: z=-0.565, p=0.5724 (consistent with random ordering)
- two_digit above/below-median: z=-0.165, p=0.8693 (consistent with random ordering)
- three_digit odd/even: z=-0.565, p=0.5724 (consistent with random ordering)
- three_digit above/below-median: z=-0.964, p=0.3348 (consistent with random ordering)

## Autocorrelation (lags 1-10)
- two_digit: 0/10 lags outside the ~95% band (±0.065); ~0-1 expected by chance alone.
- three_digit: 1/10 lags outside the ~95% band (±0.065); ~0-1 expected by chance alone.

## Interpretation
0 of 7 chi-square tests were significant at alpha=0.05. With 7 tests at alpha=0.05, roughly 0.4 false positives are expected by chance alone — a single isolated significant result is not strong evidence of bias. A consistent pattern across positions, prize categories, and separate time windows would be needed before concluding the draw is not fair.
None of this measures predictability. A perfectly fair process can still show one 'significant' test out of several by chance — that is the expected multiple-testing effect, not a flaw.