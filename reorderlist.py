# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        previoous = None
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        new_head = slow.next
        slow.next = None
        nextNode = new_head.next
        new_head.next = None
        while nextNode:
            old_head = new_head
            new_head = nextNode
            nextNode = nextNode.next
            new_head.next = old_head
        ptr = head
        ptr2 = new_head
        while ptr and ptr2:
            next_ptr = ptr.next
            next_ptr2 = ptr2.next
            ptr.next = ptr2
            ptr2.next = next_ptr
            ptr2 = next_ptr2
            ptr = next_ptr