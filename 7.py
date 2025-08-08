# How to import keyword module
import keyword

# How to print kwlist
print(keyword.kwlist)
# Expected Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# (Note: The exact list might vary slightly depending on your Python version, e.g., 'async' and 'await' were added in Python 3.5)

# How to print number of keywords
print(len(keyword.kwlist))
# Expected Output: 35 (for Python 3.8 and above, as of July 2025)
# (The number of keywords depends on the Python version. For example, it was 33 before async/await).

# How to print type of kwlist
print(type(keyword.kwlist))
# Expected Output: <class 'list'>
# Explanation: `keyword.kwlist` is a Python list containing string representations of keywords.

# Based on your last line, and assuming only 'import keyword' was used:
print(id(keyword.kwlist))
# Output: NameError: name 'kwlist' is not defined
# Explanation: When you use `import keyword`, the `kwlist` object becomes an attribute of the `keyword` module. To access it, you must use `keyword.kwlist`. If you wanted to use `kwlist` directly, you would need to import it specifically like `from keyword import kwlist`. Since `kwlist` is not defined in the global namespace here, a `NameError` occurs.

