# -*- coding: utf-8 -*-
# __author__ = 'summer'

def knapsack(lst1, lst2, W):
    """
    :param lst1:list for value
    :param lst2:list for weight
    :param w: package capacity
    :return: max value sum
    """
    dp = [[0]*(W + 1) for j in xrange(len(lst1) + 1)]
    for i in xrange(1, len(lst1) + 1):
        for j in xrange(1, len(dp[i])):
            if j < lst2[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], lst1[i - 1] + dp[i - 1][j - lst2[i - 1]])
    return dp[-1][-1]

def knapsack_1(lst1, lst2, W):
    dp = [0 for i in xrange(W + 1)]
    for i in xrange(1, len(lst1) + 1):
        for j in xrange(W, -1, -1):
            if j < lst2[i - 1] or dp[j] >= dp[j - lst2[i - 1]] + lst1[i - 1]:
                continue
            else:
                dp[j] = dp[j - lst2[i - 1]] + lst1[i - 1]
    return dp[-1]

def completeKnapsack(lst1, lst2, W):
    dp = [0 if not i else -1 for i in xrange(W + 1)]
    for i in xrange(1, len(lst1) + 1):
        for v in xrange(W, -1, -1):
            if v >= lst2[i - 1] and (dp[v] != -1 or dp[v - lst2[i - 1]] != -1):
                dp[v] = max(dp[v - lst2[i - 1]] + lst1[i - 1], dp[v])
        print dp
    return dp[-1]

print completeKnapsack([10, 20, 30], [5, 5, 5], 10)
print knapsack_1([2201, 3158, 653, 3043, 1204], [2201, 3158, 653, 3043, 1204], 5129) * 1024


