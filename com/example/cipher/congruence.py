# -*- coding: utf-8 -*-
# __author__ = 'summer'

from gcd import gcd

def congruence(a, b, m): #ax ≡ b (mod m)
    result = []
    d = gcd(a, m)
    if b % d != 0:
        return "None"
    else:
        a = a / d
        b = b / d
        m = m / d
        while b % a:
            b = b + m
        fin = b / a
        for i in xrange(d):
            result.append([fin + i * m])
        return str(result)


print congruence(243, 909, 198)