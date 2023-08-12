#!/usr/bin/python3
"""computes the length of the cl arguments and prints them out"""


import sys


def printArg():
    arg = sys.argv[1:]
    print('{} arguments:'.format(len(arg)))
    if len(arg) >= 1:
        i = 0
        for i in range(len(arg)):
            print('{} : {}'.format(i + 1, arg[i]))
    else:
        print('.')


if __name__ == '__main__':
    printArg()
