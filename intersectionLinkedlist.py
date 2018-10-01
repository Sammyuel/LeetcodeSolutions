# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        ptr1 = headA
        ptr2 = headB
        countA = 0 
        countB = 0 
        while ptr1:
            countA += 1
            ptr1 = ptr1.next
        while ptr2:
            countB += 1
            ptr2 = ptr2.next

        ptr1 = headA if countA > countB else headB
        ptr2 = headB if countB < countA else headA
        count = abs(countA - countB)
        while count > 0:
            ptr1 = ptr1.next
            count -=1 
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1 if ptr1 else None