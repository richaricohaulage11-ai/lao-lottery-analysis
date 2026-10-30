# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0344, p=0.2247 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0177, p=0.9324 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0212, p=0.7959 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.565 bits, max=6.644 bits, ratio=0.9881
- three_digit: entropy=9.062 bits, max=9.966 bits, ratio=0.9093

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=991.369, p=0.2561, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=964.497, p=0.4803, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=939.312, p=0.7016, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=948.378, p=0.6254, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=99.799, p=0.0767, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=75.371, p=0.6555, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=86.441, p=0.3190, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.100, p=0.8461, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.223, p=0.7144, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.507, p=0.2546, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.531, p=0.8187, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.723, p=0.6809, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.