# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0324, p=0.3957 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0161, p=0.9877 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0246, p=0.7393 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.549 bits, max=6.644 bits, ratio=0.9858
- three_digit: entropy=8.888 bits, max=9.966 bits, ratio=0.8919

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=585.665, p=0.4845, dof=585, groups=66 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=598.431, p=0.3412, dof=585, groups=66 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=587.561, p=0.4625, dof=585, groups=66 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=587.677, p=0.4611, dof=585, groups=66 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=54.685, p=0.1527, dof=45, groups=6 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=45.053, p=0.4697, dof=45, groups=6 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=58.296, p=0.0882, dof=45, groups=6 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=32.216, p=0.9236, dof=45, groups=6 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=10.124, p=0.9278, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.590, p=0.2507, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=13.180, p=0.7808, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=17.967, p=0.4578, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.