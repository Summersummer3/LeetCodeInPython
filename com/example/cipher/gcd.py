# -*- coding: utf-8 -*-
# __author__ = 'summer'

def gcd(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x < y:
        return gcd(y, x)
    else:
        if y % x == 0:
            return x
        else:
            return gcd(y, x-y)