# -*- coding: utf-8 -*-
# __author__ = 'summer'
from primitive_test import primitive_test
from factorization import factorization

def euler_function(x):
    """
    euler_function is to count a number has how many numbers less than itself comprime to it.
    e(m) = e(p1 ** d1) * e(p2 ** d2) * ....
    =(p1 ** (d1 - 1) * (p1 - 1)) * (p2 ** (d2 - 1) * (p2 - 1)) * .....
    :param x:int
    :return:int
    """
    if x < 2:
        return None
    if primitive_test(x):
        return x - 1
    factor_list = factorization(x)
    prime_list = []
    for factor_tuple in factor_list:
        prime_list.append(factor_tuple[0])
    for prime in prime_list:
        x = x / prime * (prime - 1)
    return x

print euler_function(11200)