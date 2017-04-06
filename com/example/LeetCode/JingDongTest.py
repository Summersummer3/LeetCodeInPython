# -*- coding: utf-8 -*-
# __author__ = 'summer'

def findSol(lst1, lst2, w0, h0):
    fpos = 0
    pos = 0
    res = []
    min_area = -1
    for r, v in enumerate(lst1):
        if v > w0 and lst2[r] > h0:
            if min_area == -1:
                min_area = v * lst2[r]
                fpos = r + 1
                pos = r + 1
            elif min_area > v * lst2[r]:
                min_area = v * lst2[r]
                pos = r + 1


    while pos:
        res.append(str(pos))
        w0 = lst1[pos - 1]
        h0 = lst2[pos - 1]
        lst1[pos - 1] = 0
        lst2[pos - 1] = 0
        pos = 0
        min_area = -1
        for r, v in enumerate(lst1):
            if v > w0 and lst2[r] > h0:
                if min_area == -1:
                    min_area = v * lst2[r]
                    fpos = r + 1
                    pos = r + 1
                elif min_area > v * lst2[r]:
                    min_area = v * lst2[r]
                    pos = r + 1

    if fpos:
        res[-1] = str(fpos)
    return res

def knapsack_1(lst1, lst2, W):
    res = []
    n = len(lst1)

    if n * 2 < W:
        res = [str(m) for m in range(1, n)]
        return sum(lst1), " ".join(res)

    pos = [0]*n
    dp = [[0]*(W + 1) for k in xrange(n + 1)]
    for i in xrange(1, n + 1):
        for j in xrange(1, W + 1):
            if j >= lst2[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - lst2[i - 1]] + lst1[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    while n > 0:
        if dp[n][W] > dp[n - 1][W]:
            pos[n - 1] = 1
            W -= lst2[n - 1]
        n -= 1
    for p in xrange(len(pos)):
        if pos[p]:
            res.append(str(p + 1))
    return dp[-1][-1], " ".join(res)

if __name__ == '__main__':
    while True:
        n, w0, h0 = [int(t) for t in raw_input().strip().split()]
        lst1 = []
        lst2 = []
        for i in xrange(n):
            w, h = [int(t) for t in raw_input().strip().split()]
            lst1.append(w)
            lst2.append(h)
        res = findSol(lst1, lst2, w0, h0)
        print(len(res))
        if len(res):
            print " ".join(res)
        else:
            print ""


# if __name__ == '__main__':
#     while True:
#         lst1 = []
#         lst2 = []
#         n, W = [int(t) for t in raw_input().strip().split()]
#         for i in xrange(n):
#             w, v = [int(t) for t in raw_input().strip().split()]
#             lst1.append(v)
#             lst2.append(w)
#         V, fstr = knapsack_1(lst1, lst2, W)
#         if not V:
#             print V
#             print "no"
#         else:
#             print V
#             print fstr



