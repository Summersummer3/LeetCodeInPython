# -*- coding: utf-8 -*-
# __author__ = 'summer'
print "wtf"


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res = [True]
        if s is None or len(s) == 0:
            return True

        for i in xrange(len(s)):
            for j in xrange(i+1):
                if res[j] and s[j:i+1] in wordDict:
                    res.append(True)
                    break
            else:
                res.append(False)
            print res
        return res[-1]


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak("a", ["a"])