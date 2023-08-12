#!/usr/bin/python3
"""computes the length of the cl arguments and prints them out"""


import sys


def printArg():
    arg = sys.argv[1:]
    if len(arg) >= 1:
        print('{} arguments:'.format(len(arg)))
        i = 0
        for i in range(len(arg)):
            print('{} : {}'.format(i + 1, arg[i]))
    else:
        print('{} arguments.'.format(len(arg)))


if __name__ == '__main__':
    printArg()
