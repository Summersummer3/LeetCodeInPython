# -*- coding: utf-8 -*-
# __author__ = 'summer'
def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    result = []
    strlst = []
    length = 0
    for word in words:

        length = length + len(word)

        if not length + len(strlst)> maxWidth:
            strlst.append(word)
        else:
            blank = maxWidth - (length - len(word))
            result.append(extend(strlst, split(blank, strlst)))
            strlst = [word]
            length = len(word)

    blank = maxWidth - length
    str = ""
    for s in strlst:
        blank = blank - 1
        if blank >= 0:
            str = str + s + " "
        else:
            str = str + s
    str = str + blank * " "
    result.append(str)
    return result

def extend(strlst, blklst):
    str = ""
    if not len(strlst) - 1:
        str = strlst[0] + blklst[0] * " "
    else:
        for s in range(0, len(strlst) - 1):
            str = str + strlst[s] + blklst[s] * " "
        str = str + strlst[-1]
    return str

def split(blank, strlst):
    blklst = []
    if not len(strlst) - 1:
        blklst.append(blank)
    else:
        for i in xrange(0, len(strlst) - 1):
            pos = len(strlst) - 1 - i
            if pos == 1:
                blklst.append(blank)
            elif not blank % pos:
                for j in xrange(i, len(strlst) - 1):
                    blklst.append(blank/pos)
                break
            else:
                blklst.append(blank/pos + 1)
                blank = blank - (blank/pos + 1)
    return blklst


print(fullJustify(["a"], 2))