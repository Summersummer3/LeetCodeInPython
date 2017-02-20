__author__ = 'summer'
def combine(n, k):
    list = range(1, n+1)
    list_pos = range(k)
    list_pos_index = k - 1
    result = []
    arr = []

    while not list_pos_index < 0:
        for each in list_pos:
            arr.append(list[each])
        result.append(arr[0:])
        arr = []
        while list_pos_index >= 0:
            if list_pos[list_pos_index] + 1 < n - (k - list_pos_index - 1):
                list_pos[list_pos_index] += 1
                while list_pos_index < k - 1:
                    list_pos[list_pos_index + 1] = list_pos[list_pos_index] + 1
                    list_pos_index += 1
                break
            else:
                list_pos_index -= 1

    return result

def combinations(list, k):
    result = []
    if k == 1:
        for each in list:
            result.append([each])
        return result

    for i in xrange(0, len(list) - k + 1):
        arr = [list[i],]
        for j in combinations(list[i+1:], k - 1):
            result.append(arr + j)
    return result


def compare(str, cStr):
    res = []
    for s_1 in str:
        for s_2 in cStr:
            if s_2 in res:
                break
            for i in range(0, len(s_1)):
                if s_1[i] not in s_2:
                    break
                if i == len(s_1) - 1:
                    res.append(s_2)
    return res



str = [[1, 4, 7], [3, 6, 7], [2, 5, 7], [1, 2, 6], [2, 3, 4], [1, 3, 5], [4, 5, 6]]

cStr = combine(7, 4)

print compare(str, cStr)