class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return 
        while head and head.val == val:
            head = head.next
        ptr = head
        previous = None 
        while ptr:
            if ptr.val == val:
                previous.next = ptr.next
            else:
                previous = ptr
            ptr = ptr.next
        return head