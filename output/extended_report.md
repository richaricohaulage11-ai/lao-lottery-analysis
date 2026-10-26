# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0339, p=0.2381 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0178, p=0.9284 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0216, p=0.7815 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.564 bits, max=6.644 bits, ratio=0.9880
- three_digit: entropy=9.057 bits, max=9.966 bits, ratio=0.9088

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=983.251, p=0.3180, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=959.953, p=0.5217, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=939.607, p=0.6992, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=945.414, p=0.6510, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=98.090, p=0.0951, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=75.020, p=0.6661, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=87.845, p=0.2825, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.976, p=0.8487, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.285, p=0.7103, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.761, p=0.2428, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.834, p=0.8014, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.904, p=0.6685, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.