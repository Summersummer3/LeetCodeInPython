_author__ = 'summer'
def canJumpRecursion(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    index = 0
    last_index = len(nums) - 1
    if index == last_index:
        return True
    steps = nums[index]
    origin_index = index

    while steps > 0:
        index = index + steps
        if index >= last_index:
            return True

        if nums[index]:
            if canJump(nums[index:]):
                return True
            else:
                print "back steps:" + str(steps)
                steps -= 1
                index = origin_index
        else:
            print steps
            steps -= 1
            index = origin_index
    print False     # how to Judge the wrong condition
    return False


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    farest = 0
    for i in xrange(len(nums)):
        if i > farest:
            return False
        jump = nums[i]
        if i + jump > farest:
            farest = i + jump
    return True

print canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,1])