# -*- coding: utf-8 -*-
# __author__ = 'summer'

def leastTime(lst):
    lst = [t / 1024 for t in lst]
    all = sum(lst)
    capacity = all // 2
    dp = [0] * (capacity + 1)
    for num in lst:
        for k in xrange(capacity, -1, -1):
            if k < num or dp[k] >= (dp[k - num] + num):
                continue
            else:
                dp[k] = dp[k - num] + num
    return (all - dp[-1]) * 1024

