class Solution(object):
    def deleteDuplicates(self, head):
        values = {}
        ptr = head
        while ptr:
            values[ptr.val] = values.get(ptr.val, 0) + 1
            ptr = ptr.next
        ptr = head
        previous = None
        while ptr:
            if values[ptr.val] > 1:
                if previous:
                    previous.next = ptr.next
                else:
                    head = ptr.next
            else:
                previous = ptr
            ptr = ptr.next
        return head