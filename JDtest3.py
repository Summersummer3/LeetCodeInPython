# -*- coding: utf-8 -*-
# __author__ = 'summer'
# if __name__ == '__main__':
#     while True:
#         n = int(raw_input())
#         arr = raw_input()
#         s = set()
#         for r, v in enumerate(arr):
#             if v != "X" and v != "#":
#                 p = int(v)
#                 while p > 0:
#                     if r - p >= 0 and arr[r - p] == "X":
#                         s.add(r - p)
#                     if r + p < len(arr) and arr[r + p] == "X":
#                         s.add(r + p)
#                     p -= 1
#         print len(s)

if __name__ == '__main__':
    while True:
        n = int(raw_input())
        fpos = []
        lpos = []
        for i in xrange(n):
            x, l = [int(t) for t in raw_input().strip().split()]
            fpos.append(x)
            lpos.append(l + x)

        ins = []
        s = set()
        print fpos, lpos
        for j in xrange(len(fpos)):
            for k in xrange(j + 1, len(fpos)):
                if fpos[j] <= lpos[k] <= lpos[j] or lpos[k] >= lpos[j] >= fpos[k]:
                    ins.append([j, k])
        print ins
        while len(ins) != 2:
            pass

        for a in ins:
            for b in a:
                s.add(b)

        print len(s)


