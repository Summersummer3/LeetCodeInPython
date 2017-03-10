# -*- coding: utf-8 -*-
# __author__ = 'summer'

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)

    b = 0
    i = 1
    while nums[b] != nums[-1]:
        if nums[i] != nums[b]:
            nums[b + 1] = nums[i]
            b = b + 1
        i = i + 1
    nums[b + 1] = nums[-1]
    return b + 1, nums[:b + 1]

print removeDuplicates([1])