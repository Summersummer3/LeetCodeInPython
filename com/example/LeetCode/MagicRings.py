# -*- coding: utf-8 -*-
# __author__ = 'summer'

if __name__ == '__main__':
    n, k = [int(t) for t in raw_input().strip().split()]
    arr = [int(t) for t in raw_input().strip().split()]
    for i in xrange(k):
        arr0 = arr[0]
        for j in xrange(len(arr)):
            if j == len(arr) - 1:
                arr[j] += arr0
            else:
                arr[j] += arr[j + 1]
            if arr[j] >= 100:
                arr[j] = arr[j] % 100
    res = [str(t) for t in arr]
    print " ".join(res)