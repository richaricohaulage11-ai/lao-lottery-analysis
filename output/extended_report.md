# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0475, p=0.3174 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0490, p=0.2828 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0222, p=0.9868 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.485 bits, max=6.644 bits, ratio=0.9761
- three_digit: entropy=8.229 bits, max=9.966 bits, ratio=0.8258

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=282.186, p=0.2928, dof=270, groups=31 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=350.787, p=0.0007, dof=270, groups=31 -> distribution DIFFERS across month (p < 0.05) [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=267.037, p=0.5395, dof=270, groups=31 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=297.439, p=0.1207, dof=270, groups=31 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=16.596, p=0.5510, dof=18, groups=3 -> distribution consistent across year
- four_digit position 1 by year: chi2=20.437, p=0.3088, dof=18, groups=3 -> distribution consistent across year
- four_digit position 2 by year: chi2=28.523, p=0.0545, dof=18, groups=3 -> distribution consistent across year
- four_digit position 3 by year: chi2=21.112, p=0.2738, dof=18, groups=3 -> distribution consistent across year

### By weekday
- four_digit position 0 by weekday: chi2=16.562, p=0.5534, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=27.421, p=0.0714, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=19.385, p=0.3685, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=25.887, p=0.1024, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.