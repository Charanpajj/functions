import math

print(math.gcd(12 , 15))
# Output: 3
# Explanation: The greatest common divisor of 12 and 15 is 3.

print(math.gcd(12 , 18))
# Output: 6
# Explanation: The greatest common divisor of 12 and 18 is 6.

print(math.gcd(4 , 7))
# Output: 1
# Explanation: The greatest common divisor of 4 and 7 is 1 (they are coprime).

print(math.gcd(7 , 7))
# Output: 7
# Explanation: The greatest common divisor of a number with itself is the number itself.

print(math.gcd(-18 , -27))
# Output: 9
# Explanation: `math.gcd()` works with the absolute values of the numbers. The GCD of 18 and 27 is 9.

print(math.gcd(-4 , 6))
# Output: 2
# Explanation: The GCD of the absolute values of -4 and 6 (i.e., 4 and 6) is 2.

print(math.gcd(0 , 7))
# Output: 7
# Explanation: The GCD of 0 and any non-zero integer `x` is `abs(x)`.

print(math.gcd(3 , 0))
# Output: 3
# Explanation: The GCD of any non-zero integer `x` and 0 is `abs(x)`.

print(math.gcd(0 , 0))
# Output: 0
# Explanation: By definition, `math.gcd(0, 0)` is 0.

#print(gcd(5 , 15))
# Output: NameError: name 'gcd' is not defined
# Explanation: `gcd()` is part of the `math` module and must be accessed using `math.gcd()`.
# Calling it directly without the `math.` prefix (or importing it specifically as `from math import gcd`)
# results in a `NameError`. The program execution stops at this line.


