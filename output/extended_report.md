# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0348, p=0.2118 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0164, p=0.9621 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0209, p=0.8099 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.565 bits, max=6.644 bits, ratio=0.9881
- three_digit: entropy=9.061 bits, max=9.966 bits, ratio=0.9092

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=998.183, p=0.2730, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=973.015, p=0.4848, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=948.441, p=0.6997, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=955.618, p=0.6400, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=100.762, p=0.0677, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.849, p=0.6712, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=86.586, p=0.3152, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=66.793, p=0.8720, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.667, p=0.6847, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.016, p=0.2313, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.279, p=0.8325, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.052, p=0.6584, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.