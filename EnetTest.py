# -*- coding: utf-8 -*-
# __author__ = 'summer'

def score():
    m, n = [int(t) for t in raw_input().strip().split()]
    res = 0
    s_1 = set()
    s_2 = []

    for s in raw_input().strip().split():
        s_1.add(s)

    for c in raw_input().strip().split():
        s_2.append(c)

    for str in s_1:
        if str in s_2:
            res += len(str) ** 2

    return res

def changeTimes(lst):
    print lst
    times = 0
    i = 0
    end = False

    while i < len(lst) - 1:
        if lst[i] != lst[i + 1]:
            j = i + 2
            if j <= len(lst) - 1:
                while lst[j] != lst[i]:
                    j += 1
                    if j == len(lst):
                        end = True
                        break
            if end:
                break
            tmp = lst[j]
            for n in xrange(j, i, -1):
                lst[n] = lst[n - 1]
            lst[i + 1] = tmp
            print i, j, lst
            times += (j - i - 1)
            i += 1
        else:
            i += 1
    print times
    return times

def countTimes(str):
    times = 0
    count = 0
    for i in xrange(len(str)):
        if not i:
            stay = str[i]
        elif str[i] != stay:
            count += 1
        else:
            times += count
    return times


if __name__ == '__main__':
    lst_1 = []
    lst_2 = []
    s = raw_input()
    for c in s:
        lst_1.append(c)
        lst_2.append(c)
    lst_2.reverse()
    print min(changeTimes(lst_1), changeTimes(lst_2))
    print countTimes(s)





