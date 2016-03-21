# -*- coding: utf-8 -*-
# __author__ = 'summer'

def extendedEuclidean(a, b): # ax + by = gcd(a, b)
    if b > a:
        return extendedEuclidean(b, a)
    org_devided = a
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    r = a % b
    q = a / b
    while r > 0:
        t_tmp = t0 - t * q
        t0 = t
        t = t_tmp
        s_tmp = s0 - s * q
        s0 = s
        s = s_tmp
        a = b
        b = r
        r = a % b
        q = a / b
    r = b
    while t < 0:
        t += org_devided
    return r, s, t

def multiplicativeInverse(a, b):  # return b^-1 that b^-1 * b ≡ 1 (mod a)
    res = extendedEuclidean(a, b)
    if res[0] == 1:
        return res[2]
    else:
        return None