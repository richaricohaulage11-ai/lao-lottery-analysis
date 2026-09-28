# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0347, p=0.2239 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0199, p=0.8599 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0236, p=0.6899 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.561 bits, max=6.644 bits, ratio=0.9875
- three_digit: entropy=9.045 bits, max=9.966 bits, ratio=0.9076

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=967.284, p=0.3753, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=951.953, p=0.5126, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=928.723, p=0.7152, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=936.615, p=0.6499, dof=954, groups=107 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=95.469, p=0.1299, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=74.689, p=0.6760, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=92.205, p=0.1855, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.135, p=0.8655, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=13.777, p=0.7435, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.153, p=0.2717, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.620, p=0.8137, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.952, p=0.5959, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.