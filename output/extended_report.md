# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0331, p=0.2669 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0204, p=0.8379 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0222, p=0.7520 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.562 bits, max=6.644 bits, ratio=0.9877
- three_digit: entropy=9.052 bits, max=9.966 bits, ratio=0.9083

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=980.090, p=0.3437, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=964.412, p=0.4811, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=944.921, p=0.6552, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=943.763, p=0.6650, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=97.988, p=0.0963, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.787, p=0.6731, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=89.765, p=0.2366, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.341, p=0.8410, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.380, p=0.7040, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.132, p=0.2262, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.421, p=0.8247, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.476, p=0.6291, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.