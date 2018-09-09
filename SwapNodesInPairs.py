# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        ptr = head
        previousPair = None
        head = head.next
        while ptr:
            first = ptr 
            second = ptr.next
            if ptr.next == None:
                previousPair.next = ptr
                break
            ptr = ptr.next.next 
            second.next = first
            first.next = None
            if previousPair:
                previousPair.next = second
            previousPair = first 
        return head