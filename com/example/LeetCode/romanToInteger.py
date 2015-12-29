__author__ = 'summer'
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    num = 0
    dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
    for i in xrange(len(s) - 1):
        if dic[s[i]] < dic[s[i + 1]]:
            num -= dic[s[i]]
        else:
            num += dic[s[i]]
    num += dic[s[-1]]
    return num


print romanToInt("CMXCIX")