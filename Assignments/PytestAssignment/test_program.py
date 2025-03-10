import pytest
from program import divide_numbers, reverse_string, get_list_element


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5.00
    assert divide_numbers(7, 3) == 2.33
    assert divide_numbers(-8, 2) == -4.00
    assert divide_numbers(9, 4) == 2.25
    assert divide_numbers(100, 25) == 4.00
    with pytest.raises(ZeroDivisionError):
        divide_numbers(5, 0)

# Test reverse_string (3 cases)
def test_reverse_string():
    assert reverse_string("Hello") == "OLLEh"
    assert reverse_string("PyTest") == "TSEtYp"
    assert reverse_string("123abcABC") == "cbaCBA321"

# Test get_list_element (3 cases)
def test_get_list_element():
    lst = ["a", "b", "c", "d"]
    assert get_list_element(lst, 1) == "b"
    assert get_list_element(lst, 3) == "d"
    with pytest.raises(IndexError):
        get_list_element(lst, 5)
