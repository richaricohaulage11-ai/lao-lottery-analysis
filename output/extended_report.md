# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0335, p=0.2544 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0201, p=0.8520 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0227, p=0.7291 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.561 bits, max=6.644 bits, ratio=0.9876
- three_digit: entropy=9.049 bits, max=9.966 bits, ratio=0.9080

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=979.404, p=0.3494, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=963.727, p=0.4873, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=944.399, p=0.6596, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=943.741, p=0.6652, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=97.415, p=0.1033, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=73.761, p=0.7033, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=91.294, p=0.2036, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.285, p=0.8422, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.182, p=0.7171, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=20.977, p=0.2806, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.020, p=0.8462, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.403, p=0.6342, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.