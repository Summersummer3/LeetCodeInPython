__author__ = 'summer'
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    for each in s:
        if each not in t:
            return False
        else:
            t = t.replace(each, "" , 1)
    return True

print isAnagram("", "")

def isAnagram_2(s, t):
    if len(s) != len(t):
        return False
    for each in set(s):
        if s.count(each) != t.count(each):
            return False
    return True

print isAnagram_2("anagram", "nagaram")