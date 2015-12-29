__author__ = 'summer'
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    arr = []
    i = 0
    j = 0
    k = 0
    limit = (m+n)/2

    if m == 0:
        if n % 2 == 0:
            return float(nums2[n/2]+nums2[n/2 - 1])/2
        else:
            return float(nums2[n/2])

    if n == 0:
        if m % 2 == 0:
            return float(nums1[m/2]+nums1[m/2 - 1])/2
        else:
            return float(nums1[m/2])

    if (m+n)%2 == 0:
        if limit == 1:
            arr.extend(nums1)
            arr.extend(nums2)
            return float(arr[-1] + arr[-2])/2
        flag = 2
    else:
        flag = 1

    while k <= limit:
        if i==m:
            arr.extend(nums2[j:j+limit+1-len(arr)])
            break

        if j==n:
            arr.extend(nums1[i:i+(limit+1-len(arr))])
            break

        if nums1[i] <= nums2[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j += 1
        k += 1
    print arr

    if flag == 2:
        return float(arr[-1] + arr[-2])/2
    else:
        return float(arr[-1])

nums1 = [2]
nums2 = [1,3,4]

print findMedianSortedArrays(nums1,nums2)