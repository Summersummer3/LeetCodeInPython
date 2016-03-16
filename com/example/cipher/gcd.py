# -*- coding: utf-8 -*-
# __author__ = 'summer'

def gcd_1(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x < y:
        return gcd_1(y, x)
    else:
        if y % x == 0:
            return x
        else:
            return gcd_1(y, x-y)

def gcd(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x < y:
        return gcd(y, x)
    res = x - (x / y) * y
    if not res:
        return y
    else:
        return gcd(y, res)

print gcd(135, 45)
print gcd_1(135, 45)
