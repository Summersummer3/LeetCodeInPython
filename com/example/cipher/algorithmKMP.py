# -*- coding: utf-8 -*-
# __author__ = 'summer'

def kmp(s, c):
    """
    :param s: original str
    :param c: pattern str
    :return: int: compare times
    """
    if not len(c):
        return 0

    pos = pos_generate(c)
    i = 0
    j = 0
    count = 0
    while i < len(s) and j < len(c):
        if pos[j] == -1 and s[i] != c[j]:
            i += 1
        elif pos[j] != -1 and s[i] != c[j]:
            if s[i] != c[pos[j]]:
                j = pos[pos[j]]
            else:
                j = pos[j]
        else:
            i += 1
            j += 1

        if j == len(c):
            count += 1
            if len(s) - i >= len(c):
                j = 0
    return count



def pos_generate(str):
    pos = [-1]
    for i in xrange(1, len(str)):
        suffix = ""
        prefix = ""
        length = 0
        s = str[:i]
        for i in xrange(0, len(s) - 1):
            prefix = prefix + s[i]
            suffix = suffix + s[-i]
            if suffix == prefix:
                length = len(prefix)
        pos.append(length)
    return pos

print pos_generate("")

print kmp("coder coder&coder", "coder")



