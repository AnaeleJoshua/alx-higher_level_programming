#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position in a new list
    without modifying the original list (like in C)
    def new_in_list(my_list, idx, element):
    If idx is negative, the function should not modify anything,
    and returns the original list
    If idx is out of range (> of number of element in my_list),
    the function should not modify anything, and returns the original list
    You are not allowed to import any module
    You are not allowed to use try/except
    """
    new_list = my_list.copy()
    if (idx < 0):
        return new_list
    elif (idx > len(new_list)):
        return new_list
    else:
        value = new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list
