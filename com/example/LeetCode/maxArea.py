__author__ = 'summer'
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i = 0
    j = len(height) - 1
    max_area = 0
    while i < j:
        if height[i] < height[j]:
            flag = height[i]
            area = (j - i) * height[i]
            i += 1
            while height[i] < flag:
                i += 1
        else:
            flag = height[j]
            area = (j - i) * height[j]
            j -= 1
            while height[j] < flag:
                j -= 1
        if area > max_area:
            max_area = area

    return max_area

height = [10,6,2,11,5,7,7]
print maxArea(height)