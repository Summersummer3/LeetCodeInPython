# -*- coding: utf-8 -*-
# __author__ = 'summer'

def luckyString(str):
    """
    Microsoft coding test
    :param str:
    :return:
    """
    res = []

    fb = [1, 1]
    while fb[-1] < 26:
        fb.append(fb[-1] + fb[-2])

    for i in xrange(len(str)):
        j = i
        while j <= len(str):
            count = 0
            last = ""
            for s in str[i:j]:
                if not s in last:
                    count += 1
                    last += s
            if count in fb and str[i:j] not in res:
                res.append(str[i:j])
            j += 1
    res.sort()
    for p in res:
        print p

def input_test():
    n = int(raw_input())
    return n

if __name__ == '__main__':
    for i in range(input_test()):
        s = raw_input().strip().strip()


