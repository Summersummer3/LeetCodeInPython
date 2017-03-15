# -*- coding: utf-8 -*-
# __author__ = 'summer'
import Queue

class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, data):
        self.q = Queue.Queue()
        self.root = TreeNode(data, None, None)
        self.add_point = self.root

    def append(self, data):
        if not self.add_point.left:
            self.add_point.left = TreeNode(data, None, None)
            if data != None:
                self.q.put(self.add_point.left)
        elif not self.add_point.right:
            self.add_point.right = TreeNode(data, None, None)
            if data != None:
                self.q.put(self.add_point.right)
        else:
            self.add_point = self.q.get()
            self.append(data)


def bfs(t):
    queue = Queue.Queue()
    node = t.root
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        if node.data != None:
            print node.data
        if node.left != None:
            queue.put(node.left)
        if node.right != None:
            queue.put(node.right)

def bfsForPhase(t):
    queue_1 = Queue.Queue()
    queue_2 = Queue.Queue()
    flag = 1
    node = t.root
    queue_1.put(node)
    while (flag == 1 and not queue_1.empty()) or (flag == 2 and not queue_2.empty()):
        output = ""
        res = []
        if flag == 1:
            while not queue_1.empty():
                node = queue_1.get()
                if node.data != None:
                    res.append(node.data)
                if node.left != None:
                    queue_2.put(node.left)
                if node.right != None:
                    queue_2.put(node.right)
            flag = 2
        else:
            while not queue_2.empty():
                node = queue_2.get()
                if node.data != None:
                    res.append(node.data)
                if node.left != None:
                    queue_1.put(node.left)
                if node.right != None:
                    queue_1.put(node.right)
            flag = 1
        for i in res:
            output = output + str(i) + "    "
        print output


t = BinaryTree(1)
t.append(3)
t.append(5)
t.append(7)
t.append(9)
t.append(11)

bfsForPhase(t)
