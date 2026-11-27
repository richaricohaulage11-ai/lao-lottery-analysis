# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0337, p=0.2387 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0157, p=0.9743 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0204, p=0.8289 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.567 bits, max=6.644 bits, ratio=0.9885
- three_digit: entropy=9.066 bits, max=9.966 bits, ratio=0.9097

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=997.025, p=0.2817, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=972.728, p=0.4874, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=952.703, p=0.6647, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=964.610, p=0.5608, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=101.568, p=0.0608, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.813, p=0.6723, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=86.062, p=0.3293, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.696, p=0.8333, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.794, p=0.7424, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.529, p=0.2093, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.475, p=0.8218, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.868, p=0.6710, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.