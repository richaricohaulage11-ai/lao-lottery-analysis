# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0350, p=0.2056 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0169, p=0.9518 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0218, p=0.7657 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.565 bits, max=6.644 bits, ratio=0.9881
- three_digit: entropy=9.060 bits, max=9.966 bits, ratio=0.9091

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=1007.560, p=0.2084, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=971.584, p=0.4977, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=947.639, p=0.7061, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=954.305, p=0.6512, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=100.228, p=0.0726, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=73.796, p=0.7023, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=87.023, p=0.3036, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=66.814, p=0.8716, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.331, p=0.7073, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.196, p=0.2234, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.260, p=0.8335, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.247, p=0.6449, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.