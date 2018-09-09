# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        ptr = head
        beforeNode = None
        nextNode = None
        counter = 1
        stack = []
        while (counter != m):
            beforeNode = ptr
            ptr = ptr.next
            counter += 1 
        while (counter != n+1):
            stack.append(ptr)
            ptr = ptr.next
            counter +=1 
        nextNode = ptr
        while stack:
            if beforeNode == None:
                head = stack.pop(len(stack)-1)
                beforeNode = head
            else:
                beforeNode.next = stack.pop(len(stack)-1)
                beforeNode = beforeNode.next
        beforeNode.next = nextNode
        return head
            