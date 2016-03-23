# -*- coding: utf-8 -*-
# __author__ = 'summer'
def decimalToOther(n, m):
    """
    n decimal integer
    m radix number
    :param n: int
    :param m: int
    :return: int
    """
    res = ""
    while n > m:
        res = str(n % m) + res
        n /= m
    res = str(n) + res
    return int(res)

def decimalToBinary(n):
    """
    as the function name
    :param n:int
    :return:binary int
    """
    return decimalToOther(n, 2)
