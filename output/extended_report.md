# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0342, p=0.2313 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0172, p=0.9451 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0214, p=0.7888 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.565 bits, max=6.644 bits, ratio=0.9881
- three_digit: entropy=9.059 bits, max=9.966 bits, ratio=0.9090

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=986.886, p=0.2894, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=961.210, p=0.5102, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=939.675, p=0.6987, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=947.124, p=0.6363, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=98.894, p=0.0861, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=75.386, p=0.6551, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=87.213, p=0.2987, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=68.184, p=0.8443, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.091, p=0.7231, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.689, p=0.2461, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.507, p=0.8200, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=14.557, p=0.6921, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.