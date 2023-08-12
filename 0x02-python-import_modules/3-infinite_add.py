#!/usr/bin/python3
"""sums all command line argument"""


import sys


def sumCommandLine():
    """sums all command line arg assuming they are all integer"""
    args = sys.argv[1:]
    sumList = sum([int(arg) for arg in args])
    print('\n\n {}'.format(sumList))


if __name__ == '__main__':
    sumCommandLine()
