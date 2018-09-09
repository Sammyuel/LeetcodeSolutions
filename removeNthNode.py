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
        container = []
        previous = head
        ptr = head
        counter = 1
        while ptr:
            container.append(ptr)
            ptr = ptr.next
        deleteNode = len(container)-1 - (n-1)
        if deleteNode == 0:
            return head.next 
        beforeNode = container[deleteNode-1]
        if n > 1:
            beforeNode.next = container[deleteNode + 1]
        else:
            beforeNode.next = None
        return head
        