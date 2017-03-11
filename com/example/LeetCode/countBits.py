# -*- coding: utf-8 -*-
# __author__ = 'summer'
def countBits(num):
    res = []
    exp = 0
    for i in xrange(0, num + 1):
        if exp == 0:
            res.append(i)
        elif i < 2 ** exp + 2 ** (exp - 1):
            res.append(res[i - 2 ** (exp - 1)])
        else:
            res.append(res[i - 2 ** (exp - 1)] + 1)
        if i == 2 ** (exp + 1) - 1:
            exp = exp + 1
    return res

print countBits(0)