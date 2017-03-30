# -*- coding: utf-8 -*-
# __author__ = 'summer'
def lastLength():
    lst = raw_input().strip().split()
    return len(lst[-1])

def countTimesOfStr():
    str = raw_input().strip()
    c = raw_input().strip()
    count = 0
    for s in str:
        if c == s:
            count += 1
        elif abs(ord(c) - ord(s))== ord("a") - ord("A"):
            count += 1
    return count

def setTest(n):
    i = 0
    s = set()
    while i < n:
        j = int(raw_input())
        s.add(j)
        i += 1
    lst = list(s)
    lst.sort()
    for a in lst:
        print a


if __name__ == '__main__':
    while(True):
        try:
            n = int(raw_input())
            setTest(n)
        except:
            break