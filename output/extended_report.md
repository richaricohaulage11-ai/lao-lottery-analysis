# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0335, p=0.2478 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0150, p=0.9834 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0213, p=0.7875 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.565 bits, max=6.644 bits, ratio=0.9882
- three_digit: entropy=9.061 bits, max=9.966 bits, ratio=0.9092

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=1006.713, p=0.2138, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=975.897, p=0.4588, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=949.896, p=0.6879, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=962.440, p=0.5802, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=100.255, p=0.0723, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.331, p=0.6866, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=85.655, p=0.3405, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.216, p=0.8639, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.651, p=0.7515, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.493, p=0.2108, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.110, p=0.8415, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.879, p=0.6703, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.