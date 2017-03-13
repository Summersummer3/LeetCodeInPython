# -*- coding: utf-8 -*-
# __author__ = 'summer'
def myMap(str):
    """
    :param str: string
    :return
    """
    res = ""
    my_map = []
    for s in str:
        n = len(my_map)
        if not n:
            my_map.append(ord(s))
            res = res + s
        elif not binarySearch(0, n - 1, ord(s), my_map):
            my_map.append(ord(s))
            res = res + s
            my_map = sorted(my_map)
    return res

def binarySearch(m, n, tgt, arr):
    r = False
    while m <= n:
        if arr[m + (n - m) / 2] == tgt:
            r = True
            break
        elif arr[m + (n - m) / 2] < tgt:
            m = m + (n - m) / 2 + 1
        else:
            n = n - (n - m) / 2 - 1
    return r

arr = [97, 98, 99]
print binarySearch(0, len(arr) - 1, 97, arr)
print(myMap("Team_Secret!!"))