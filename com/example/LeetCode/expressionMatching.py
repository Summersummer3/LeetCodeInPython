__author__ = 'summer'
def isMatchSubString(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    j = 0
    s_length = len(s)
    p_length = len(p)

    if s_length == 0 or p_length == 0:
        return False

    for i in xrange(p_length):
        if p[i] == s[j] or p[i] == ".":
            match_flag = i
            while j < s_length:
                if match_flag == p_length:
                    return False
                if p[match_flag] != s[j] and p[match_flag] != "." and p[match_flag] != "*":
                    if match_flag + 1 < p_length:
                        if p[match_flag + 1] != "*":
                            j = 0
                            break
                        else:
                            j -= 1
                    else:
                        j = 0
                        break

                if p[match_flag] == "*":
                    if p[match_flag - 1] == s[j] or p[match_flag - 1] == ".":
                        match_flag -= 1    #fix the p's index when match no less than 1 time the previous number of *
                    else:
                        print "here"
                        j -= 1

                match_flag += 1
                j += 1

            if j == s_length:
                return True

    return False

def isMatch(s,p):
    i = 0
    j = 0
    count = 0
    s_length = len(s)
    p_length = len(p)

    if s_length == 0 or p_length == 0:
        return False

    while j < s_length and i < p_length:
        print (j,i)
        if p[i] != s[j] and p[i] != "." and p[i] != "*":
            if i + 1 < p_length:
                if p[i + 1] != "*":
                    j = 0
                    break
                else:
                    j -= 1
        if p[i] == s[j] == s[-1]:
            if i + 1 < p_length:
                if p[i + 1] != "*":
                        count += 1
        if p[i] == "*":
            if p[i - 1] == s[j] or p[i - 1] == ".":
                i -= 1    #fix the p's index when match no less than 1 time the previous number of *
            else:
                print "here"
                j -= 1

        i += 1
        j += 1

    while i < p_length and i + 1 < p_length:
        print i

        while p[i] == "*" or p[i + 1] == "*":
            i += 1
            if i + 1 == p_length:
                if p[i] == "*":
                    i += 1
                break

        while i < p_length:
            if p[i] == s[-1] or p[i] == ".":
                i += 1
                count += 1
                print "here"
                if count > s_length:
                    return False
            else:
                break



    if i < p_length and i + 1 == p_length:
        if p[i] == "*":
            i += 1

    if j == s_length and i == p_length:
        return True
    else:
        return False


print isMatch("abcdeff", ".*")
