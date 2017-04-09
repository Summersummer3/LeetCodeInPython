# -*- coding: utf-8 -*-
# __author__ = 'summer'

import cmath

if __name__ == '__main__':
    while True:
        n, m = [int(t) for t in raw_input().strip().split()]
        total = 0.00
        while m > 0:
            total += n
            n = cmath.sqrt(n)
            m -= 1
        print total
        # int1, int2 = [int(t) for t in raw_input().strip().split()]
        # res = []
        # for i in xrange(int1, int2 + 1):
        #     total = 0
        #     str1 = str(i)
        #     for j in str1:
        #         total += int(j) ** 3
        #     if total == i:
        #         res.append(str(i))
        # if len(res):
        #     print " ".join(res)
        # else:
        #     print "no"