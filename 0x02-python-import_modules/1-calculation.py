#!/usr/bin/python3
"""carries out math operations on any two numbers"""


from calculator_1 import add, sub, mul, div


a = 10
b = 5

if __name__ == '__main__':
    print('{} + {} = {}'.format(a,b,add(a,b)))
    print('{} - {} = {}'.format(a,b,sub(a,b)))
    print('{} * {} = {}'.format(a,b,mul(a,b)))
    print('{} / {} = {}'.format(a,b,div(a,b)))
