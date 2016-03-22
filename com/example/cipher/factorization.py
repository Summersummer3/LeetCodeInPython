# -*- coding: utf-8 -*-
# __author__ = 'summer'
from primitive_test import primitive_test
import math

def factorization(x):
    """
    x is an integer need to be factorized as this form:
    x = p1 ** i1 * p2 ** i2 * ....
    use the list [(p1, i1),(p2, i2)...]  as the result.
    take long time to factorize a big integer,how to improve ?
    :param x: int
    :return: list
    """
    res = []
    prime_list = []
    for n in xrange(2, int(math.sqrt(x) + 1)):
        if primitive_test(n):
            prime_list.append(n)
    for factor in prime_list:
        degree = 0
        while x % factor == 0:
            degree += 1
            x /= factor
        if degree:
            res.append((factor, degree))
        if x in prime_list:
            res.append((x, 1))
            return res
        if x == 1:
            return res
