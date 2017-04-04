# -*- coding: utf-8 -*-
# __author__ = 'summer'

if __name__ == '__main__':
    n = int(raw_input())
    tX = [int(t) for t in raw_input().strip().split()]
    tY = [int(t) for t in raw_input().strip().split()]
    gx, gy = [int(t) for t in raw_input().strip().split()]
    walkTime, taxiTime = [int(t) for t in raw_input().strip().split()]

    for i in xrange(len(tX)):
        cost = min((abs(tX[i]) + abs(tY[i])) * walkTime + (abs(gx - tX[i]) + abs(gy - tY[i])) * taxiTime,
                   (abs(gx) + abs(gy)) * walkTime)
        if not i:
            minTime = cost
        elif minTime > cost:
            minTime = cost
    print minTime