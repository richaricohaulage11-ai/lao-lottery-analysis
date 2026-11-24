# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0335, p=0.2456 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0152, p=0.9810 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0205, p=0.8222 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.567 bits, max=6.644 bits, ratio=0.9885
- three_digit: entropy=9.065 bits, max=9.966 bits, ratio=0.9097

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=999.287, p=0.2649, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=972.898, p=0.4858, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=951.330, p=0.6762, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=960.033, p=0.6016, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=102.770, p=0.0517, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=75.787, p=0.6428, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=85.531, p=0.3440, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.310, p=0.8417, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.422, p=0.7659, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.318, p=0.2182, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.479, p=0.8216, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.526, p=0.6942, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.