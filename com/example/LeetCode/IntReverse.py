__author__ = 'summer'
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    MAX_INT = 2147483647  # when you do in a test,you need to consider the limit size of int is 2^31

    if x <= 0:
        flag = -1
        x = 0 - x
    else:
        flag = 1

    arr = []
    n = len(str(x)) - 1

    while n >= 0:
        arr.append(str(x/(10**n)))
        x = x % (10**n)
        n -= 1

    arr.reverse()
    result = int("".join(arr))
    if flag == -1 and result <= MAX_INT:
        return -result
    if result <= MAX_INT:  # you need judge if it over the limit! in fact int in python is not limit...
        return int("".join(arr))
    else:
        return 0

print reverse(1646324353)