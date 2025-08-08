# max() and min() functions demo program
from builtins import max , min
# Explanation: `max()` and `min()` are built-in functions in Python, so explicitly importing them from `builtins` is not necessary, but it's a valid way to confirm their origin.

print(max(10.8 , 20.6))
# Output: 20.6
# Explanation: `max()` returns the largest of the given arguments. 20.6 is greater than 10.8.

print(min(10.8 , 20.6 , 5.9 , 12.3))
# Output: 5.9
# Explanation: `min()` returns the smallest of the given arguments. 5.9 is the smallest among the provided floats.

print(max(25 , 10.8))
# Output: 25
# Explanation: `max()` correctly compares integers and floats. 25 is greater than 10.8.

import builtins
# Explanation: This imports the `builtins` module, which contains all Python's built-in functions.

print(builtins.max(10 , 20 , 30))
# Output: 30
# Explanation: Accessing `max()` via the `builtins` module works correctly. 30 is the largest integer among 10, 20, and 30.

print(builtins.min(10 , 20 , 15 , 5 , 12))
# Output: 5
# Explanation: Accessing `min()` via the `builtins` module works correctly. 5 is the smallest integer among 10, 20, 15, 5, and 12.


