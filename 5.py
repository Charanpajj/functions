# pow() function demo program
from builtins import pow
# Explanation: `pow()` is a built-in function, always available. This explicit import is optional.

print(pow(10 , -2))
# Output: 0.01
# Explanation: `pow(base, exp)` calculates `base` raised to the power of `exp`.
# `10` to the power of `-2` is $10^{-2} = 1 / 10^2 = 1 / 100 = 0.01$.

print(pow(4 , pow(3 , 2)))
# Output: 262144
# Explanation: When `pow()` is nested, the inner `pow()` call is evaluated first.
# 1. `pow(3, 2)` evaluates to $3^2 = 9$.
# 2. The expression then becomes `pow(4, 9)`.
# 3. `pow(4, 9)` evaluates to $4^9 = 262144$.
# This behavior is consistent with the right-to-left associativity of the `**` operator.

import builtins
# Explanation: This imports the `builtins` module, which holds all Python's built-in functions.

print(builtins . pow(2 , 3))
# Output: 8
# Explanation: Accessing `pow()` via the `builtins` module works correctly. $2^3 = 8$.

print(builtins . pow(-2 , -3))
# Output: -0.125
# Explanation: `-2` to the power of `-3` is $(-2)^{-3} = 1 / (-2)^3 = 1 / (-8) = -0.125$.

