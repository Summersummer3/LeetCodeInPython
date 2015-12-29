__author__ = 'summer'
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    n = numRows
    key = 0
    loop_limit = 2 * n - 2

    if loop_limit == 0:
        return s

    dic = dict()
    dic_key = 0

    for i in range(1,n+1):
        dic[i] = list()

    while key < len(s):
        left = (key + 1) % loop_limit
        if left > n or left == 0:
            if left == 0:
                left = loop_limit
            dic_key = n - (left - n)
        else:
            dic_key = left
        dic[dic_key].append(s[key])
        key += 1

    for j in range(2, n+1):
        dic[1].extend(dic[j])

    return "".join(dic[1])

s = "abcd"
n = 3

print convert(s, n)
