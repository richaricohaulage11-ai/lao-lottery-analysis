# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0351, p=0.2110 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0198, p=0.8657 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0232, p=0.7057 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.559 bits, max=6.644 bits, ratio=0.9873
- three_digit: entropy=9.043 bits, max=9.966 bits, ratio=0.9074

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=972.241, p=0.3335, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=949.276, p=0.5371, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=928.889, p=0.7139, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=936.644, p=0.6497, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=97.063, p=0.1077, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.091, p=0.6937, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=92.354, p=0.1826, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.245, p=0.8634, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.817, p=0.7410, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.135, p=0.2727, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.211, p=0.8362, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.727, p=0.6116, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.