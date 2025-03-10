def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")  # ✅ Fix: Handling division by zero
    return round(a / b, 2)

def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")  # ✅ Fix: Prevents non-string input
    return ''.join([char.swapcase() for char in s[::-1]])

def get_list_element(lst, index):
    """Returns the element at the given index in the list, or raises an IndexError."""
    if index >= len(lst) or index < 0:
        raise IndexError("Index out of range")  # ✅ Fix: Proper boundary check with exception
    return lst[index]
