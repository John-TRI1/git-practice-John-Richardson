def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    result = a / b  # Bug: No handling for division by zero
    return round(result, 2)


def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    reversed_s = s[::-1]  # Bug: Might not handle non-string input properly
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case


def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not found' if out of range."""
    if index < len(lst):  # Bug: Incorrect boundary check
        return lst[index]
    else:
        return "Not found"  # Bug: Should probably raise an exception instead