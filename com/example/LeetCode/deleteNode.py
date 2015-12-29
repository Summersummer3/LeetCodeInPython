__author__ = 'summer'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    while node!= None:
        if node.next.next:
            node.val = node.next.val
        else:
            node.val = node.next.val
            node.next = None
        node = node.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

deleteNode(node2)

node = node1
while node!= None:
    print node.val
    node = node.next