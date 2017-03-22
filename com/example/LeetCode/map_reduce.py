# -*- coding: utf-8 -*-
# __author__ = 'summer'

def normalize(name):
    return capitalize_2(name)

def capitalize(str):
    res = ""
    for i in xrange(len(str)):
        if not i:
            res += str[i].upper()
        else:
            res += str[i].lower()
    return res

def normalize_2(name):
    return name.capitalize()

def capitalize_2(str):
    res = ""
    for i in xrange(len(str)):
        if not i:
            if ord(str[i]) >= ord("a"):
                res += chr(ord(str[i]) - ord("a") + ord("A"))
            else:
                res += str[i]
        else:
            if ord(str[i]) <= ord("Z"):
                res += chr(ord(str[i]) + ord("a") - ord("A"))
            else:
                res += str[i]
    return res

def prod(L):
    return reduce(lambda x, y: x * y, L)

def str2float(s):
    dot_pos = 0
    for i in s:
        if i == ".":
            break
        dot_pos += 1
    if not dot_pos:
        sum_1 = 0
    elif dot_pos == 1:
        sum_1 = int(s[0])
    else:
        s_1 = s[:dot_pos]
        sum_1 = reduce(lambda x, y: x * 10 + y, map(int, s_1))

    s_2 = s[dot_pos + 1: len(s)]
    l_2 = map(int, s_2)
    l_2.reverse()
    sum_2 = reduce(lambda x, y: x * 0.1 + y, l_2) * 0.1

    return sum_1 + sum_2



L1 = ['adam', 'LISA', 'barT']

print map(normalize, L1)
print map(normalize_2, L1)
print prod([1, 2, 3, 4])
print str2float("123.345000")