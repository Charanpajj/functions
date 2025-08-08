import math

print(math.floor(10.8))
# Output: 10
# Explanation: `math.floor()` returns the largest integer less than or equal to the given number. For 10.8, the largest integer less than or equal to it is 10.

print(math.ceil(10.8))
# Output: 11
# Explanation: `math.ceil()` returns the smallest integer greater than or equal to the given number. For 10.8, the smallest integer greater than or equal to it is 11.

print(math.floor(25.0))
# Output: 25
# Explanation: For a whole number, `floor()` returns the number itself.

print(math.ceil(25.0))
# Output: 25
# Explanation: For a whole number, `ceil()` returns the number itself.

print(math.floor(-3.5))
# Output: -4
# Explanation: `floor()` rounds down towards negative infinity. The largest integer less than or equal to -3.5 is -4.

print(math.ceil(-3.5))
# Output: -3
# Explanation: `ceil()` rounds up towards positive infinity. The smallest integer greater than or equal to -3.5 is -3.

print(math.floor(-9.0))
# Output: -9
# Explanation: For a whole negative number, `floor()` returns the number itself.

print(math.ceil(-9.0))
# Output: -9
# Explanation: For a whole negative number, `ceil()` returns the number itself.

print(math.floor(25.1))
# Output: 25
# Explanation: The largest integer less than or equal to 25.1 is 25.

print(math.ceil(25.1))
# Output: 26
# Explanation: The smallest integer greater than or equal to 25.1 is 26.

print(floor(3.5))
# Output: NameError: name 'floor' is not defined
# Explanation: `floor()` is part of the `math` module and must be accessed using `math.floor()`. Calling it directly without the `math.` prefix (or importing it specifically as `from math import floor`) results in a `NameError`. The program execution stops here.


