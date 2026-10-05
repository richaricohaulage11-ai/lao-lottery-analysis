# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.0342, p=0.2354 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.0202, p=0.8460 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.0231, p=0.7135 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=6.560 bits, max=6.644 bits, ratio=0.9874
- three_digit: entropy=9.046 bits, max=9.966 bits, ratio=0.9077

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- four_digit position 0 by month: chi2=979.723, p=0.3468, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 1 by month: chi2=959.199, p=0.5285, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 2 by month: chi2=939.569, p=0.6995, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]
- four_digit position 3 by month: chi2=945.601, p=0.6494, dof=963, groups=108 -> distribution consistent across month [LOW SAMPLE WARNING]

### By year
- four_digit position 0 by year: chi2=96.886, p=0.1100, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 1 by year: chi2=73.733, p=0.7041, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 2 by year: chi2=91.621, p=0.1970, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]
- four_digit position 3 by year: chi2=67.367, p=0.8610, dof=81, groups=10 -> distribution consistent across year [LOW SAMPLE WARNING]

### By weekday
- four_digit position 0 by weekday: chi2=14.125, p=0.7209, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 1 by weekday: chi2=21.659, p=0.2475, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 2 by weekday: chi2=12.446, p=0.8234, dof=18, groups=3 -> distribution consistent across weekday
- four_digit position 3 by weekday: chi2=15.283, p=0.6425, dof=18, groups=3 -> distribution consistent across weekday

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.