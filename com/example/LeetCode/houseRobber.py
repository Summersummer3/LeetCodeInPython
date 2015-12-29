__author__ = 'summer'
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    index = 1
    dp = []
    dp.append(nums[0])
    if len(nums) > 1:
        dp.append(max(nums[0],nums[1]))
    for each in nums[2:]:
        dp.append(max(dp[index], (dp[index - 1] + each)))
        index += 1
    return dp[-1] if len(nums) > 1 else dp[0]


print rob([])