#!/usr/bin/python3


def no_c(my_string):
    """Write a function that removes all characters c and C from a string.

    Prototype: def no_c(my_string):
    The function should return the new string
    You are not allowed to import any module
    You are not allowed to use str.replace()
    """
    for i in my_string:
       # print(i)
        if (i == "c" or i == "C"):
            i = ""
            return my_string

