# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0373, p=0.5972 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0282, p=0.8865 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0507, p=0.2296 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.451 bits, max=6.644 bits, ratio=0.9709
- three_digit: entropy=8.275 bits, max=9.966 bits, ratio=0.8304

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=314.710, p=0.2297, dof=297, groups=34 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=309.268, p=0.3002, dof=297, groups=34 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=291.950, p=0.5718, dof=297, groups=34 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=299.043, p=0.4558, dof=297, groups=34 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=43.782, p=0.0218, dof=27, groups=4 -> distribution DIFFERS across year (p < 0.05) [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=26.967, p=0.4656, dof=27, groups=4 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=32.556, p=0.2121, dof=27, groups=4 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=23.154, p=0.6767, dof=27, groups=4 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=7.829, p=0.9811, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=25.168, p=0.1204, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=11.182, p=0.8865, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=22.125, p=0.2265, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.