# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0337, p=0.2451 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0185, p=0.9091 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0217, p=0.7743 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.564 bits, max=6.644 bits, ratio=0.9879
- three_digit: entropy=9.054 bits, max=9.966 bits, ratio=0.9085

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=980.798, p=0.3379, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=962.263, p=0.5006, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=941.809, p=0.6813, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=944.291, p=0.6605, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=97.393, p=0.1035, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=75.676, p=0.6462, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=88.763, p=0.2600, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.050, p=0.8471, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.267, p=0.7115, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.948, p=0.2343, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.853, p=0.8003, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.067, p=0.6574, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.