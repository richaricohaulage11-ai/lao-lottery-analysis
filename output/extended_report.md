# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0354, p=0.2057 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0201, p=0.8540 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0239, p=0.6740 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.560 bits, max=6.644 bits, ratio=0.9874
- three_digit: entropy=9.040 bits, max=9.966 bits, ratio=0.9071

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=972.434, p=0.3319, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=947.035, p=0.5575, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=929.578, p=0.7084, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=937.505, p=0.6423, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=94.930, p=0.1381, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=73.903, p=0.6992, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=90.435, p=0.2218, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=66.629, p=0.8750, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.018, p=0.7905, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=20.529, p=0.3039, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.915, p=0.7966, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=16.259, p=0.5745, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.