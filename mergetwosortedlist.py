# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = l1
        not_head = l2
        if l1.val > l2.val:
            head = l2
            not_head = l1
        ptr = head.next
        ptr2 = not_head
        previous = head
        while ptr and ptr2:
            if ptr.val >= ptr2.val:
                ptr2_continue = ptr2.next
                previous.next = ptr2
                ptr2.next = ptr
                previous = ptr2
                ptr2 = ptr2_continue
            else:
                previous = ptr
                ptr = ptr.next
        if ptr2:
            previous.next = ptr2
        return head