#!/usr/bin/python3


def element_at(my_list, idx):
    if (idx < 0):
        return None
    elif (idx > len(my_list)):
            return None
    else:
        value = my_list.pop(idx)
        my_list.insert(idx,value)
        return value
