# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0344, p=0.2286 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0207, p=0.8254 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0229, p=0.7213 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.561 bits, max=6.644 bits, ratio=0.9875
- three_digit: entropy=9.046 bits, max=9.966 bits, ratio=0.9077

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=979.858, p=0.3457, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=968.930, p=0.4404, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=937.415, p=0.7167, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=944.381, p=0.6598, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=96.868, p=0.1103, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=73.542, p=0.7096, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=91.843, p=0.1926, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.593, p=0.8565, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.070, p=0.7245, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.357, p=0.2618, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.592, p=0.8152, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.175, p=0.6499, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.