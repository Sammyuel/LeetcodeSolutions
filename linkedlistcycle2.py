# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        while head != fast:
            head = head.next
            fast = fast.next
        return head