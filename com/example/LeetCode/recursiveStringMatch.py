__author__ = 'summer'
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    s_length = len(s)
    p_length = len(p)

    if not s_length:
        return not bool(p_length)


    # case 1: p comes to -1:
    if p_length <= 1:
        if s_length == 0 or s_length > p_length:
            return False
        if s[0] == p[0] or p[0] == ".":
            return True
        return False

    # case 2: p[1] != "*"
    if p[1] != "*":
        if s[0] != p[0] and p[0] != ".":
            return False
        else:
            return isMatch(s[1:],p[1:])

    # case 3: p[1] == "*"
    else:
        # case 3.1: "*" is the last letter in p
        if p_length == 2:
            i = 0
            while i < s_length:
                if s[i] != p[0] and p[0] != ".":
                    return False
                i += 1
            return True

        # case 3.2: p = ".*" compare zero times
        # if isMatch(s, p[2:]):
        #     return True

        #case 3.3: p = ".*" compare 1 time
        j = -1

        while (j < s_length and (s[j] == p[0] or p[0] == "." or j < 0)):
            if isMatch(s[j + 1:],p[2:]):
                return True
            j += 1
        return False

print isMatch("aab","c*a*a*a*a*a*a*a*a*a*b")