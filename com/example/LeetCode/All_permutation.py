__author__ = 'summer'
class All_permutation:
    def __init__(self):
        self.result_arr = []


    def all_permutation(self, arr, begin, end):
        self.result_list = []
        if begin == end:
            tmp = arr[0:]
            self.result_arr.append(tmp)
        for i in xrange(begin, end + 1):
            self.swap(arr, begin, i)
            self.all_permutation(arr, begin + 1, end)
            self.swap(arr, begin, i)

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

a_p = All_permutation()
a_p.all_permutation([1, 2, 3, 4, 5], 0, 4)
print a_p.result_arr