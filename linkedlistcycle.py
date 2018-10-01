# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast != None and fast.next != None and fast != slow:
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return False
        return True
                