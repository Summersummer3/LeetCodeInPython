f = lambda x:20 if x > 20 else x
print f(10)

def combineRecusion(list, k):
    result = []
    if k == 1:
        for each in list:
            result.append([each])
        return result
    else:
        for i in xrange(len(list) - k + 1):
            arr = [list[i],]
            for each in combineRecusion(list[i+1:], k - 1):
                result.append(arr + each)
        return result

print combineRecusion(["a", "b", "c", "d"], 3)