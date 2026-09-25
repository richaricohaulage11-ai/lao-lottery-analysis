# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0356, p=0.2004 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0206, p=0.8337 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0237, p=0.6820 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.560 bits, max=6.644 bits, ratio=0.9874
- three_digit: entropy=9.042 bits, max=9.966 bits, ratio=0.9073

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=969.473, p=0.3566, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=947.422, p=0.5540, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=928.169, p=0.7195, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=938.316, p=0.6352, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=95.572, p=0.1283, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.145, p=0.6921, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=90.987, p=0.2100, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.291, p=0.8625, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.209, p=0.7790, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.110, p=0.2739, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=13.188, p=0.7803, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=16.454, p=0.5609, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.