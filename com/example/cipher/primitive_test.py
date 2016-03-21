# -*- coding: utf-8 -*-
# __author__ = 'summer'

def primitive_test(x):
    if (factorial(x - 1) + 1) % x == 0:
        return True
    else:
        return False

def factorial(x):
    base = 1
    for i in xrange(2, x + 1):
        base *= i
    return base
