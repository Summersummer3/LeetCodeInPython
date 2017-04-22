# -*- coding: utf-8 -*-
# __author__ = 'summer'

class Solution:
    stack1 = []
    stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return res

    def minNumberInRotateArray(self, rotateArray):
        if not len(rotateArray):
            return 0
        for i in xrange(len(rotateArray)):
            if i and rotateArray[i] < rotateArray[i - 1]:
                return rotateArray[i]
        return rotateArray[-1]

