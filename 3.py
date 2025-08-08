# abs() function demo program
from builtins import abs
# Explanation: The `abs()` function is a built-in function in Python, meaning it's always available
# without needing an explicit import. This 'from builtins import abs' statement is redundant but harmless.

print(abs(-35.8))
# Output: 35.8
# Explanation: `abs()` returns the absolute value of a number (its distance from zero), which is always non-negative.

print(abs(-27))
# Output: 27
# Explanation: The absolute value of -27 is 27.

print(abs(29.5))
# Output: 29.5
# Explanation: The absolute value of a positive number is the number itself.

print(abs(32))
# Output: 32
# Explanation: The absolute value of a positive integer is the integer itself.

import builtins
# Explanation: This imports the `builtins` module, which contains all Python's built-in functions and constants.

print(builtins.abs(-25))
# Output: 25
# Explanation: You can access built-in functions by explicitly referencing them through the `builtins` module,
# though it's typically unnecessary for directly available built-ins like `abs()`. The absolute value of -25 is 25.

