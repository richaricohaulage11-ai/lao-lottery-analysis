# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0337, p=0.2472 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0205, p=0.8317 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0225, p=0.7368 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.561 bits, max=6.644 bits, ratio=0.9876
- three_digit: entropy=9.047 bits, max=9.966 bits, ratio=0.9078

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=978.572, p=0.3564, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=971.631, p=0.4163, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=941.423, p=0.6844, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=947.322, p=0.6346, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=96.733, p=0.1120, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=73.712, p=0.7047, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=90.540, p=0.2195, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.613, p=0.8351, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.367, p=0.7048, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.526, p=0.2537, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.225, p=0.8354, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.751, p=0.6099, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.