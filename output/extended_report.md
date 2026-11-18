# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0339, p=0.2340 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0149, p=0.9849 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0210, p=0.8016 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.567 bits, max=6.644 bits, ratio=0.9884
- three_digit: entropy=9.063 bits, max=9.966 bits, ratio=0.9094

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=1003.987, p=0.2319, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=976.977, p=0.4492, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=949.162, p=0.6939, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=957.693, p=0.6221, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=102.121, p=0.0565, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.972, p=0.6676, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=86.594, p=0.3150, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.742, p=0.8535, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.493, p=0.7615, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.092, p=0.2279, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=11.828, p=0.8560, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.120, p=0.7212, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.