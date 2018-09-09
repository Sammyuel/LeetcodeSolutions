# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if head == None:
            return
        ptr = head
        nodes = []
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        k = k % len(nodes)
        if k == 0 or head.next == None:
            return head
        newHeadIndex = len(nodes) - 1 - (k-1)
        nodes[len(nodes) - 1].next = head 
        beforeNode = nodes[newHeadIndex - 1]
        beforeNode.next = None
        return nodes[newHeadIndex]
        
        
        