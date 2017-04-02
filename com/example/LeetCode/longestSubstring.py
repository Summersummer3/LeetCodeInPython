__author__ = 'summer'
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    arr = []
    max_len = 0

    for i, val in enumerate(s):
        if val not in arr:
            arr.append(val)
            if i + 1 == len(s):
                tmp_len = len(arr)
                max_len = max(max_len, tmp_len)
        else:
            tmp_len = len(arr)
            j = arr.index(val) + 1
            arr = arr[j:]
            arr.append(val)
            max_len = max(max_len, tmp_len)
    return max_len


print lengthOfLongestSubstring("afshkashfohiowefhowerovbhndsfovndfsiou;hvdfjklohgbvio8:rgioverbvio/:dfhjk/logbhvdfjk/ghkefhgkutrhgkejrhkjehuehghufru")