import random
def quicksort(arr,begin,end):
    if begin < end:
        middle = partition(arr, begin, end)
        quicksort(arr, begin, middle-1)
        quicksort(arr, middle+1, end)

def partition(arr,begin,end):
    position = end
    para = arr[end]
    while begin < end:
        if arr[begin] > para:
            if arr[end-1] < para:
                temp = arr[begin]
                arr[begin] = arr[end-1]
                arr[end-1] = temp
                begin += 1
                end -= 1 
            else:
                end -= 1
        else:
            begin += 1
    temp = arr[begin]
    arr[begin] = arr[position]
    arr[position] = temp
    return begin

def randomized_quicksort(arr, begin, end):
    if begin < end:
        middle = partition(arr, begin, end)
        randomized_quicksort(arr, begin, middle-1)
        randomized_quicksort(arr, middle+1, end)

def randomized_partition(arr, begin, end):
    position = random.randint(begin, end)
    para = arr[position]
    temp_1 = arr[end]
    arr[end] = para
    arr[position] = temp_1
    position = end
    while begin < end:
        if arr[begin] > para:
            if arr[end-1] < para:
                temp = arr[begin]
                arr[begin] = arr[end-1]
                arr[end-1] = temp
                begin += 1
                end -= 1
            else:
                end -= 1
        else:
            begin += 1
    temp_2 = arr[begin]
    arr[begin] = arr[position]
    arr[position] = temp_2
    return begin


            
if __name__ == '__main__':
    a = []
    for each in range(0,50):
        a.append(random.randint(0,100))
    print a
    randomized_quicksort(a, 0, len(a)-1)
    print a