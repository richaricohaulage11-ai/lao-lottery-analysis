# Extended Methods Report

## Kolmogorov-Smirnov goodness-of-fit (secondary check to chi-square)
- two_digit KS-test vs uniform[0,100): D=0.5600, p=0.1057 -> consistent with uniform
- three_digit KS-test vs uniform[0,1000): D=0.2480, p=0.9121 -> consistent with uniform
- four_digit KS-test vs uniform[0,10000): D=0.3902, p=0.4690 -> consistent with uniform

## Shannon entropy (bits) vs. maximum possible entropy
A ratio near 1.0 indicates the distribution is close to maximally random.
- two_digit: entropy=1.500 bits, max=6.644 bits, ratio=0.2258
- three_digit: entropy=2.000 bits, max=9.966 bits, ratio=0.2007

## Homogeneity across time groupings (does the pattern differ by month/year/weekday?)
### By month
- Not enough distinct month groups yet to test.

### By year
- Not enough distinct year groups yet to test.

### By weekday
- Not enough distinct weekday groups yet to test.

Interpretation: these test whether the draw's digit distribution shifts across months, years, or days of the week — a legitimate question for a physical or electronic draw mechanism, distinct from testing overall uniformity. As with the core chi-square tests, isolated significant results among many groups/positions tested are expected by chance and are not evidence of a real time-based pattern unless they replicate consistently.