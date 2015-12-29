__author__ = 'summer'
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    list = []
    result = []
    for coin in coins:
        list.append(amount - coin)
    for each in list:
        if each in coins:
            return 1
        else:
            result.append(coinChange(coins, amount - each))



