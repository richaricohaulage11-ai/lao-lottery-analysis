# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0341, p=0.2273 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0143, p=0.9903 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0209, p=0.8086 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.566 bits, max=6.644 bits, ratio=0.9883
- three_digit: entropy=9.063 bits, max=9.966 bits, ratio=0.9094

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=1001.364, p=0.2500, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=974.801, p=0.4687, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=947.572, p=0.7066, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=959.051, p=0.6102, dof=972, groups=109 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=101.592, p=0.0606, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=75.547, p=0.6501, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=86.025, p=0.3303, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.867, p=0.8509, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.520, p=0.7598, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=22.411, p=0.2143, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=11.937, p=0.8505, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.457, p=0.6989, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.