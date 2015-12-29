__author__ = 'summer'
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    dp = [1]
    if len(s) == 0:
        return 0
    if s[0] == "0":
        return 0
    if len(s) == 1:
        return 1

    if int(s[:2]) <= 26 and s[1] != "0":
        dp.append(2)
    else:
        return 0 if int(s[:2]) > 26 and s[1] == "0" else dp.append(1)

    for i in xrange(2, len(s)):
        if s[i] != "0":
            if s[i - 1] == "0":
                dp.append(dp[i - 1])
            else:
                if int(s[i-1:i+1]) <= 26:
                    dp.append(dp[i - 1] + dp[i - 2])
                else:
                    dp.append(dp[i - 1])
        else:
            if (int(s[i-1:i+1]) <= 26) and (int(s[i-1:i+1]) != 0):
                dp.append(dp[i - 2])
            else:
                return 0
    return dp[-1]

print numDecodings("301")

