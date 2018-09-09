# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head == None:
            return
        even = head.next
        evenHead = even 
        odd = head
        previous = None
        ptr = head.next
        nextNode = None
        state = True
        while ptr:
            if ptr.next:
                nextNode = ptr.next.next
            else:
                nextNode = None
            odd.next = previous 
            previous = ptr.next
            even.next = nextNode
            ptr = nextNode
            even = even.next
            if odd.next:
                odd = odd.next 
            if previous != None and ptr == None:
                odd.next = previous
                odd = odd.next
        odd.next = evenHead
        return head 
            