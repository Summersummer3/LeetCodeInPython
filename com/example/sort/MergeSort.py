
def mergesort(arr,tmp,left,right):
    if(left<right):
        middle = (left+right)/2
        mergesort(arr, tmp, left, middle)
        mergesort(arr, tmp, middle+1, right)
        merge(arr,tmp,left,middle,right)
        
def merge(arr,tmp,left,middle,right):
    
    tmp = []
    leftLoc = left
    leftEnd = middle
    rightLoc = middle + 1
    rightEnd = right 
    
    while(leftLoc <= leftEnd and rightLoc <= rightEnd):
        
        if arr[leftLoc]<arr[rightLoc]:
            tmp.append(arr[leftLoc])
            leftLoc += 1
        else:
            tmp.append(arr[rightLoc])
            rightLoc += 1
    
    if(leftLoc > leftEnd):
        while(rightLoc <= rightEnd):
            tmp.append(arr[rightLoc])
            rightLoc += 1
    else:
        while(leftLoc <= leftEnd):
            tmp.append(arr[leftLoc])
            leftLoc += 1

    for j in tmp:
        arr[left] = j
        left += 1
     
    


origin = [2,3,6,8,5,4,45]
temp = []
mergesort(origin, temp, 0, len(origin)-1)
print origin