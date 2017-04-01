# -*- coding: utf-8 -*-
# __author__ = 'summer'#

import sys


def realize(str):
    lst = list(str)
    l = len(lst)
    i = 0
    count = 0
    while count < l:
        if lst[i].isupper():
            tmp = lst[i]
            lst.remove(tmp)
            lst.append(tmp)
        else:
            i += 1
        count += 1
    return lst


def countDiff(arr):
    if len(arr) < 2:
        print 0, 0
        return
    index = []
    min = arr[1] - arr[0]
    tmp = [1]

    arr.sort()
    for i in xrange(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if not diff:
            tmp[-1] += 1
        else:
            if diff < min:
                index = [len(tmp)]
                min = diff
            elif diff == min:
                index.append(len(tmp))
            tmp.append(1)

    if len(tmp) == len(arr):
        maxCount = 1
        minCount = 0
        for j in index:
            minCount += tmp[j] * tmp[j - 1]

    else:
        maxCount = tmp[0] * tmp[-1] if len(tmp) > 1 else tmp[0] * (tmp[0] - 1) / 2
        minCount = 0
        for n in tmp:
            if n > 1:
                minCount += n * (n - 1)/2

    print minCount, maxCount

if __name__ == '__main__':
    # while True:
    #     try:
    #         n = int(raw_input())
    #         arr = [int(t) for t in raw_input().strip().split()]
    #         countDiff(arr)
    #     except:
    #         break
    # while True:
    #     s = input()
    #     if isinstance(s, str):
    #         print "".join(realize("hxKLAGLLzPyTxsFsrUnnSKQBHdQQrOyaEYJRgiJbHIDXFcQkFmIhPNKIBfHxXDBdKAvgZiBLVwnlxJAHmttsSJkZhSmQneNVoKoIYZRjPqsrFFaaqZbyNyeRjVKVFrCGdfycidTqbyQcpAtdRGzzBAaKoqybWMOyhrCQdwcRwQQpQavTnAbjriVwxJOrTYJVGYSWzKYeNAGqBzkJLucabNYvyVFxAGKLfqHXNttaqZfncEdTroGMzZnDbvZBBaRbJvuYIvlWrKaaGrvtyxrsCUOqxdwCrmVEeDrLKZKFJVRmrLsmbmOGUJyfdZIrFhuSwJQGRTYMLxKQNMaCavatlQIRZmFQvyWgQTVENxUcPKQCaUQbjyfaNuwoNdTBNldgrtPUcQodqsuJOdDpUczJWCZaasDdEYJkvituMHrCmZQSlRjIefVisatIUtfxBeKnHPyvWUKzRliFsYWgeXogiEgXDbfxAybwFuqFyEvjfIHEPDPKqEiGUtZhdDIDBGKpvBFyqHeEEhAToAbqHEpIdIhIGBtWjGHiQRctZxQQYkfFoWUbqZyIcjRPQBilHrnqNBzFmoRUYCSrGkawJCcOrMceegISpIpSGVjbngWVMTYtGoAlQFPFyOFAxndJZNfKDTwFIxisKTjyjchidXpYgLfoBOLriuIAHmAbQwoHBgbdUYBHlDQGZJASsHszOEPthLVnYbNqWegmONexfdsTVYHgtDmlyugefOBsqmgNDBoxkkhVHfvrYooVOyxDJQJLjYSngksbTopoPJFsKQzHePLukXyYTYCeW"))
    #     else:
    #         break
    s = sys.stdin.readline().strip()
    while s:
        print "".join(realize(s))
        s = sys.stdin.readline().strip()
