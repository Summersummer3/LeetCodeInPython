# -*- coding: utf-8 -*-
# __author__ = 'summer'
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

print congruence(243, 909, 198)