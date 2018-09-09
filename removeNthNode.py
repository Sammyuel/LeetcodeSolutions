# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#test 
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head == None:
            return 
        nodes = []
        previous = head
        ptr = head
        counter = 1
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        deleteNode = len(nodes)-1 - (n-1)
        if deleteNode == 0:
            return head.next 
        beforeNode = nodes[deleteNode-1]
        if n > 1:
            beforeNode.next = nodes[deleteNode + 1]
        else:
            beforeNode.next = None
        return head
        