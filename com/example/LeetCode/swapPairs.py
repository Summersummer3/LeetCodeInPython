__author__ = 'summer'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    node = head
    flag = 1

    while node != None:
        node_after_1 = node.next
        if node_after_1 != None:
            node_after_2 = node_after_1.next
            if flag == 1:
                node.next = node_after_2
                node_after_1.next = node
                head = node_after_1

            else:
                if node_after_2 != None:
                    node.next = node_after_2
                    node_after_1.next = node_after_2.next
                    node_after_2.next = node_after_1
                    node = node_after_1
                else:
                    node = node.next
        else:
            node = node_after_1
        flag = 2
        if node != None:
            print "node.value: " + str(node.val)
    return head

def swapPairsRecursive(head):
    node = head
    if node and node.next:
        node_after = node.next
        node_temp = node_after.next
        node_after.next = node
        node.next = swapPairsRecursive(node_temp)
        head = node_after
    return head

# idea of recursion should be considered! especially in sequence

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node = swapPairsRecursive(node1)
while node != None:
    print(node.val)
    node = node.next





