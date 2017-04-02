# -*- coding: utf-8 -*-
# __author__ = 'summer'

import sys

def longestSubsquence(s1, s2):
    v = 0
    dp = []
    for i in xrange(len(s1) + 1):
        dp.append([0])
        if not i:
            for j in xrange(1, len(s2) + 1):
                dp[i].append(0)
    while v < len(s1):
        w = 0
        while w < len(s2):
            if s1[v] == s2[w]:
                dp[v + 1].append(dp[v][w] + 1)
            else:
                dp[v + 1].append(max(dp[v][w], dp[v][w + 1], dp[v + 1][w]))
            w += 1
        v += 1

    return dp[-1][-1]

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    while s:
        l1 = list(s)
        l2 = list(s)
        l2.reverse()
        print len(l1) - longestSubsquence(l1, l2)
        s = sys.stdin.readline().strip()