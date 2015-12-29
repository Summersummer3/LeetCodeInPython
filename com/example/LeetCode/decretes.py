__author__ = 'summer'
array = [[1,2],[4,5],[2,3,6]]

def decretes(array):
    result = []
    if len(array) == 1:
        for i in xrange(0, len(array[0])):
            result.append([array[0][i]])
        return result

    for j in xrange(0,len(array[0])):
        arr = [array[0][j],]
        for each in decretes(array[1:]):
            result.append(arr + each)
    return result

print decretes(array)