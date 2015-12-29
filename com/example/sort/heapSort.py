import random
from __builtin__ import str

a = []
for i in range(0,10):
    a.append(random.randint(0,100))

print a

class HeapSort:
    
    arr = [-1]
    
    def __init__(self,a):
        self.arr.extend(a)
        
    def size(self):
        return len(self.arr)
    
    def parent(self,i):
        return i / 2
    
    def left(self,i):
        return i * 2
    
    def right(self,i):
        return i * 2 + 1
    
    def maxHeapify(self,i,size):
        
        largest = i
        if self.left(i) < size and self.arr[largest] < self.arr[self.left(i)]:
            largest = self.left(i)
                 
        if self.right(i) < size and self.arr[largest] < self.arr[self.right(i)]:
            largest = self.right(i) 
                
        if i != largest: 
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.maxHeapify(largest,size)
    
    def heapBuilding(self):
        for each in range (self.size()/2,0,-1):  

            self.maxHeapify(each,self.size())
            
    def heapSort(self):
        size = self.size()
        self.heapBuilding()
        for j in range (1,self.size()):
            temp = self.arr[size-1]
            self.arr[size-1] = self.arr[1]
            self.arr[1] = temp
            size -= 1
            self.maxHeapify(1, size)
            
    def __str__(self):
        self.arr.remove(-1)
        return str(self.arr)
    
hs = HeapSort(a)
hs.heapSort()

print hs
