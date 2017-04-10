# -*- coding: utf-8 -*-
# __author__ = 'summer'

def longestIncreaseSeq(arr):
    dp = [0] * len(arr)
    for r, v in enumerate(arr):
        if not r:
            dp[0] = 1
        else:
            flag = -1
            for i in xrange(r - 1, -1, -1):
                if arr[i] < v:
                    if flag == -1:
                        flag = i
                    elif dp[flag] < dp[i]:
                        flag = i

            if flag != -1:
                dp[r] = dp[flag] + 1
            else:
                dp[r] = 1

    return max(dp)


if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        m = int(raw_input())
        arr = [int(t) for t in raw_input().strip().split()]
        print longestIncreaseSeq(arr)