# -*- coding: utf-8 -*-
# __author__ = 'summer'

from gcd import gcd
from extendedEuclidean import multiplicativeInverse

def solveQuestion(a, m, b, n):
    """
    input: x = a mod m , x = b mod n, gcd(m, n) == 0
    according to ChineseReminderTheorem
    x = x * i mod m * n
    so x = k * m + a = b mod n
    k * m = b - a mod n
    use extended Euclid to get m ** -1 = i
    so: k = (b - a)*i mod n
    output: x = k * m + a
    """
    if gcd(m, n) != 1:
        return None
    k = (multiplicativeInverse(n, m) * (b - a)) % n
    return k * m + a, m * n

print solveQuestion(3, 7, 5, 15)