#!/usr/bin/python3


import sys


def sumCommandLine():
    """sums all command line arg assuming they are all integer"""
    args = sys.argv[1:]
    sumList = sum([int(arg) for arg in args])
    print(f'\n\n {sumList}')


if __name__ == '__main__':
    sumCommandLine()
