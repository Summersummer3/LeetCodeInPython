# -*- coding: utf-8 -*-
# __author__ = 'summer'
def hanoi(n, begin, middle, end):
    if n == 1:
        print "%s ==> %s" % (begin, end)
        return
    else:
        hanoi(n - 1, begin, end, middle)
        print "%s ==> %s" % (begin, end)
        hanoi(n - 1, middle, begin, end)

hanoi(3, "x", "y", "z")