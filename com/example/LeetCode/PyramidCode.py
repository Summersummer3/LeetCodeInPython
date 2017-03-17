# -*- coding: utf-8 -*-
# __author__ = 'summer'

def maxPath(prmd):
    path = []
    res = []
    pos = 0
    for i in xrange(1, len(prmd) + 1):
        tmp = []
        for j in xrange(len(prmd[-i])):
            choice = 0
            if i == 1:
                tmp.append((prmd[-i][j], 0))
            elif res[i - 2][j + 1][0] > res[i - 2][j][0]:
                choice = 1
                tmp.append((prmd[-i][j] + res[i - 2][j + 1][0], choice))
            else:
                tmp.append((prmd[-i][j] + res[i - 2][j][0], choice))
        res.append(tmp)

    path.append(prmd[0][pos])
    for k in xrange(1, len(prmd)):
        if res[-k][pos][1]:
            pos += 1
        path.append(prmd[k][pos])
    return res[-1][0][0], path



print maxPath([[7], [3, 2], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])


