# -*- coding: utf-8 -*-
# __author__ = 'summer'
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefex = ""
    if strs == []:
        return prefex
    for i in xrange(0, len(strs[0])):
        prefex = strs[0][:i + 1]
        for string in strs:
             if len(prefex) > len(string):
                return prefex[:-1]
             else:
                 if prefex != string[:i + 1]:
                     return prefex[:-1]
    return prefex

print longestCommonPrefix(["cbba", "cbbac", "cbbbc"])