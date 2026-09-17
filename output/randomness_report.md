# Randomness Test Report

Draws analyzed: 400
Date range: 2024-01-01 to 2026-07-20

Reminder: every prize category below (2 ตัวล่าง, 3 ตัวบน, 2 ตัวบน) is sliced from the SAME 4-digit draw (four_digit), not a separate random draw. See data_loader.py for exactly which digits map to which category.

## Part 1: Marginal chi-square, per digit position of four_digit
- four_digit position 0 (marginal): chi2=4.400, p=0.8832, n=400, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 1 (marginal): chi2=19.350, p=0.0224, n=400, categories=10 -> significant deviation from uniform (p < 0.05)
- four_digit position 2 (marginal): chi2=11.450, p=0.2461, n=400, categories=10 -> consistent with uniform (fails to reject randomness)
- four_digit position 3 (marginal): chi2=7.600, p=0.5749, n=400, categories=10 -> consistent with uniform (fails to reject randomness)

## Part 2: Joint/interaction chi-square on the derived prize categories
(Tests whether pairs/triples of digit positions are jointly uniform — this can catch correlation between positions that the marginal tests above would miss, even if each position looks fine on its own.)
- two_digit_bottom (00-99, joint/interaction test): chi2=108.000, p=0.2520, n=400, categories=100 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- two_digit_top (00-99, joint/interaction test): chi2=84.500, p=0.8503, n=400, categories=100 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]
- three_digit_top (000-999, joint/interaction test): chi2=1055.000, p=0.1066, n=400, categories=1000 -> consistent with uniform (fails to reject randomness) [LOW SAMPLE WARNING: expected count per category < 5]

## Runs tests
- two_digit_bottom odd/even: z=1.006, p=0.3144 (consistent with random ordering)
- two_digit_bottom above/below-median: z=-1.190, p=0.2342 (consistent with random ordering)
- two_digit_top odd/even: z=1.922, p=0.0546 (consistent with random ordering)
- two_digit_top above/below-median: z=-0.100, p=0.9206 (consistent with random ordering)

## Autocorrelation (lags 1-10)
- two_digit_bottom: 1/10 lags outside the ~95% band (±0.098); ~0-1 expected by chance alone.
- two_digit_top: 1/10 lags outside the ~95% band (±0.098); ~0-1 expected by chance alone.

## Interpretation
1 of 7 chi-square tests were significant at alpha=0.05. With 7 tests at alpha=0.05, roughly 0.4 false positives are expected by chance alone — a single isolated significant result is not strong evidence of bias. A consistent pattern across positions, prize categories, and separate time windows would be needed before concluding the draw is not fair.
None of this measures predictability. A perfectly fair process can still show one 'significant' test out of several by chance — that is the expected multiple-testing effect, not a flaw.