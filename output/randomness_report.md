# Randomness Test Report

Draws analyzed: 900
Date range: 2017-10-04 to 2026-09-23

Reminder: every prize category below (5/4/3/2 ตัว) is a trailing slice of the SAME 4-digit draw (four_digit), not a separate random draw. See data_loader.py for exactly which digits map to which category.

## Part 1: Marginal chi-square, per digit position of four_digit
- four_digit position 0 (marginal): chi2=15.689, p=0.0737, n=900, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 1 (marginal): chi2=3.956, p=0.9143, n=900, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 2 (marginal): chi2=5.378, p=0.8002, n=900, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 3 (marginal): chi2=12.267, p=0.1987, n=900, categories=10 -> consistent with uniform (fails to reject randomness)

## Part 2: Joint/interaction chi-square on the derived prize categories
- two_digit (2 digits, joint/interaction test): chi2=105.111, p=0.3182, n=900, categories=100 -> consistent with uniform (fails to reject randomness)
- three_digit (3 digits, joint/interaction test): chi2=1017.778, p=0.3327, n=900, categories=1000 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- four_digit (4 digits, joint/interaction test): chi2=10144.444, p=0.1519, n=900, categories=10000 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]

## Runs tests
- two_digit odd/even: z=-0.467, p=0.6406 (consistent with random ordering)
- two_digit above/below-median: z=-0.063, p=0.9498 (consistent with random ordering)
- three_digit odd/even: z=-0.467, p=0.6406 (consistent with random ordering)
- three_digit above/below-median: z=-0.934, p=0.3504 (consistent with random ordering)

## Autocorrelation (lags 1-10)
- two_digit: 0/10 lags outside the ~95% band (±0.065); ~0-1 expected by chance alone.
- three_digit: 1/10 lags outside the ~95% band (±0.065); ~0-1 expected by chance alone.

## Interpretation
0 of 7 chi-square tests were significant at alpha=0.05. With 7 tests at alpha=0.05, roughly 0.4 false positives are expected by chance alone — a single isolated significant result is not strong evidence of bias. A consistent pattern across positions, prize categories, and separate time windows would be needed before concluding the draw is not fair.
None of this measures predictability. A perfectly fair process can still show one 'significant' test out of several by chance — that is the expected multiple-testing effect, not a flaw.