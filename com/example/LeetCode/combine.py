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
            arr = [list[i]]
    return result



print combinations(["a","d","b","c"], 3)