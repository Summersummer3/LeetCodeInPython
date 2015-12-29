__author__ = 'summer'
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    dp =[1, 2]
    index = 2
    while len(dp) < n:
        dp.append(dp[index - 1] + dp[index - 2])
        index += 1
    return dp[0] if n == 1 else dp[-1]


print climbStairs(3)