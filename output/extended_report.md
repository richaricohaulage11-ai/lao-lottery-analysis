# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0337, p=0.2408 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0155, p=0.9773 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0212, p=0.7946 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.566 bits, max=6.644 bits, ratio=0.9882
- three_digit: entropy=9.061 bits, max=9.966 bits, ratio=0.9092

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=1003.628, p=0.2343, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=973.742, p=0.4782, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=951.132, p=0.6778, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=959.710, p=0.6044, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=101.143, p=0.0644, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.371, p=0.6854, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=86.152, p=0.3268, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.768, p=0.8529, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.682, p=0.7496, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.104, p=0.2274, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.004, p=0.8470, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.473, p=0.6978, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.