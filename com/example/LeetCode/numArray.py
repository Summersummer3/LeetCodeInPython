__author__ = 'summer'
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.array = []
        for each in nums:
            if len(self.array):
                self.array.append(self.array[-1] + each)
            else:
                self.array.append(each)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.array[j] if i == 0 else self.array[j] - self.array[i - 1]

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 2)
print numArray.sumRange(2, 5)
print numArray.sumRange(0, 5)