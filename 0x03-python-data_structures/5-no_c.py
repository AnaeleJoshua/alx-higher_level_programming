#!/usr/bin/python3


def no_c(my_string):
    """Write a function that removes all characters c and C from a string.

    Prototype: def no_c(my_string):
    The function should return the new string
    You are not allowed to import any module
    You are not allowed to use str.replace()
    """
    my_string = my_string

    a = ""
    my_string_array = [char for char in my_string if char != 'c' if char != 'C']
    return print(a.join(my_string_array).strip())


if __name__ == '__main__':
   no_c() 