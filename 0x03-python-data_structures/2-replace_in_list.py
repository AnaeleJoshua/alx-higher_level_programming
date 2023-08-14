#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position (like in C)
    Prototype: def replace_in_list(my_list, idx, element):
        If idx is negative, the function should not modify anything,
        and returns the original list
        If idx is out of range (> of number of element in my_list),
        the function should not modify anything, and returns the original list
        You are not allowed to import any module
        You are not allowed to use try/except"""
    if (idx < 0):
        return my_list
    elif (idx > len(my_list)):
        return my_list
    else:
        value = my_list.pop(idx)
        my_list.insert(idx, element)
        return my_list
