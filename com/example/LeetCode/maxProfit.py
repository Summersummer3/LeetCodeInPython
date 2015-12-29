__author__ = 'summer'
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dp = [0]
    if len(prices) < 2:
        return 0
    high = max(prices[0], prices[1])
    low = min(prices[0], prices[1])
    if prices[1] > prices[0]:
        dp.append(prices[1] - prices[0])
    else:
        dp.append(0)
    index = 1
    for each in prices[2:]:
        if each > high:
            high = each
            dp.append(high - low)
        else:
            if each > low and each - low > dp[index]:
                dp.append(each - low)
            else:
                if each < low:
                    low = each
                dp.append(dp[index])
        index += 1

    return dp[-1]

print maxProfit([6,1,3,2,4,7])