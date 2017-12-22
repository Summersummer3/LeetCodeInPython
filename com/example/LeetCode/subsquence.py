# -*- coding: utf-8 -*-
# __author__ = 'summer'

def subsequence(num):
    dp = [0] * len(num)
    dp[0] = [num[0]]
    max_l = 1
    max_i = [0]

    for i in xrange(1, len(num)):
        if num[i] > num[i - 1]:
            dp[i] = dp[i - 1][:]
            dp[i].append(num[i])

        else:
            if i == 1:
                dp[i] = [num[i]]
            else:
                j = i - 2
                while num[j] > num[i] and j >= 0:
                    j -= 1
                if j == -1:
                    dp[i] = [num[i]]
                else:
                    dp[i] = dp[j][:]
                    dp[i].append(num[i])
        if len(dp[i]) > max_l:
            max_l = len(dp[i])
            max_i = [i]
        elif len(dp[i]) == max_l:
            max_i.append(i)

    for k in max_i:
        print dp[k]

subsequence([10, 9, 2, 5, 3, 7, 101, 18])

