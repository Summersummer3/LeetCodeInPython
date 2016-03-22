# -*- coding: utf-8 -*-
# __author__ = 'summer'
from decimalChange import decimalToBinary

def squareAndMultiply(mes, n, b):
    """
    :param mes: int, the message
    :param n: int, = p * q
    :param b: int, key, we need to count mes ** b
    :return: e int, res = mes ** b (mod n)
    """
    e = 1
    pk = str(decimalToBinary(b))
    for bit in pk:
        i = int(bit)
        e = (e ** 2) % n
        if i:
            e = (e * mes) % n
    return e

print squareAndMultiply(9726, 11413, 3533)
