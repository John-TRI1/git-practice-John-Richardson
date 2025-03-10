# Fixes for Bugs in `program.py`

## Bug: No Handling for Division by Zero in `divide_numbers()`
###  What was the bug?
The function `divide_numbers(a, b)` did not check if `b == 0`, leading to a `ZeroDivisionError` when dividing by zero.

###  How was it identified?
This issue was discovered by running tests where `b = 0`, which caused the program to crash.

### 🛠 Fix Applied
Added a check to **raise a `ZeroDivisionError`** if `b == 0`.
```python
if b == 0:
    raise ZeroDivisionError("Cannot divide by zero")
