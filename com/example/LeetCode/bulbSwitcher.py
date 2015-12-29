__author__ = 'summer'
import time
def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    result = 0
    bulbs = []
    for i in xrange(0, n):
        bulbs.append(False)
    for j in xrange(1, n+1):
        k = j - 1
        while k < len(bulbs):
            bulbs[k] = not bulbs[k]
            k = k + j
    for each in bulbs:
        if each:
            result += 1
    return result

print bulbSwitch(999999)