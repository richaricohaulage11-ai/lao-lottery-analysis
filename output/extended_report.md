# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0329, p=0.2745 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0210, p=0.8104 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0224, p=0.7444 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.562 bits, max=6.644 bits, ratio=0.9877
- three_digit: entropy=9.050 bits, max=9.966 bits, ratio=0.9081

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=977.545, p=0.3651, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=967.320, p=0.4548, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=948.473, p=0.6246, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=945.478, p=0.6504, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=97.355, p=0.1040, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.235, p=0.6895, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=90.166, p=0.2276, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.645, p=0.8344, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.235, p=0.7137, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.825, p=0.2399, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.573, p=0.8163, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.372, p=0.6363, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.