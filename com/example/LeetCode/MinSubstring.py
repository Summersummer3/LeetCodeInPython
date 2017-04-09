# -*- coding: utf-8 -*-
# __author__ = 'summer'
"""
any two chars in str2 should not be identical.

"""

def minSubtring(str1, str2):
    lst = list(str2)
    pos = [-1] * len(str2)
    length, s, t = 0, 0, 0

    for i, c in enumerate(str1):
        if c in lst:
            pos[lst.index(c)] = i
        if -1 not in pos and (not length or length > max(pos) - min(pos)):
            s = min(pos)
            t = max(pos)
            length = t - s
    if length:
        return str1[s: t + 1]
    else:
        return "no"

if __name__ == '__main__':
    str1 = raw_input()
    str2 = raw_input()
    print minSubtring(str1, str2)

