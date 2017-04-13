# -*- coding: utf-8 -*-
# __author__ = 'summer'

def intPow(a, n):
    """ 
    :return: a ** n 
    """
    res = 1
    flag = False
    if n < 0:
        n = -n
        flag = True
    while n > 0:
        if n & 1:
            res *= a
        a *= a
        n = n >> 1
    if flag:
        return 1.0 / res
    return res

def matrixMulti(a, b):
    res = [[0] * len(b[0]) for t in xrange(len(a))]
    for i in xrange(len(a)):
        for j in xrange(len(b[0])):
            for k in xrange(len(a[0])):
                res[i][j] += a[i][k] * b[k][j]
            if res[i][j] > 99:
                res[i][j] = res[i][j] % 100
    return res

def matrixPow(a, b, n):
    if len(a) != len(a[0]):
        return -1
    res = b
    while n > 0:
        if n & 1:
            res = matrixMulti(res, a)
        a = matrixMulti(a, a)
        n = n >> 1
    return res


#only square matrix can do pow()
# def matrixPow(a, n):
#     if len(a) != len(a[0]):
#         return -1
#     res = [[0] * len(a[0]) for t in xrange(len(a))]
#     # generate E matrix
#     for i in xrange(len(a)):
#         res[i][i] = 1
#     while n > 0:
#         if n & 1:
#             res = matrixMulti(a, res)
#         a = matrixMulti(a, a)
#         n = n >> 1
#     return res

#magic rings with O(n^3(logk))
#original one is O(nk), since k is much large than n^3

if __name__ == '__main__':
    # a, n = [int(t) for t in raw_input().strip().split()]
    # print intPow(a, n)
    # print matrixMulti([[1, 2],[3, 4]], [[1, 2, 3], [2, 3, 4]])
    # print matrixPow([[1, 2], [2, 1]], 3)
    n, k = [int(t) for t in raw_input().strip().split()]
    arr = [[int(t) for t in raw_input().strip().split()]]
    mtx = [[0]*len(arr[0]) for t in xrange(len(arr[0]))]
    for i in xrange(len(arr[0])):
        mtx[i][i] = 1
        if i != len(arr[0]) - 1:
            mtx[i + 1][i] = 1
        else:
            mtx[0][i] = 1
    res = matrixPow(mtx, arr, k)
    res = [str(t) for t in res[0]]
    print " ".join(res)
