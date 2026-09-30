# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0349, p=0.2174 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0193, p=0.8842 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0234, p=0.6978 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.560 bits, max=6.644 bits, ratio=0.9874
- three_digit: entropy=9.043 bits, max=9.966 bits, ratio=0.9074

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=966.548, p=0.3816, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=951.329, p=0.5183, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=927.393, p=0.7256, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=936.714, p=0.6491, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=95.197, p=0.1340, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.627, p=0.6778, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=92.853, p=0.1733, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.265, p=0.8630, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.625, p=0.7532, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.287, p=0.2652, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.399, p=0.8260, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.800, p=0.6065, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.