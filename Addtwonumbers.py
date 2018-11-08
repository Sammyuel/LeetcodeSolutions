# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_head = l1
        l2_head = l2
        l1_stack = []
        l2_stack = []
        head = ListNode(1)
        while l1 or l2:
            if l1:
                l1_stack.append(l1)
                l1 = l1.next
            if l2:
                l2_stack.append(l2)
                l2 = l2.next
        remainder = 0 
        longer = l1_stack if len(l1_stack) > len(l2_stack) else l2_stack
        shorter = l2_stack if len(l2_stack) < len(l1_stack) else l1_stack
        while longer:
            first = longer.pop(-1) 
            second = shorter.pop(-1).val if shorter else 0 
            if first.val + second + remainder>= 10:
                first.val = (first.val + second + remainder) % 10 
                remainder = 1
            else:
                first.val = first.val + second + remainder
                remainder = 0 
        if remainder:
            head.next = first
            return head
        return first

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        len1, len2 = self.getLength(l1), self.getLength(l2)
        l1 = self.addLeadingZeros(len2-len1, l1)
        l2 = self.addLeadingZeros(len1-len2, l2)
        c, ans = self.combineList(l1, l2)
        if c>0:
            l3 = ListNode(c)
            l3.next = ans
            ans = l3
        return ans

    def getLength(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l

    def addLeadingZeros(self, n, node):
        for i in range(n):
            new = ListNode(0)
            new.next = node
            node = new
        return node

    def combineList(self, l1, l2):
        if (not l1 and not l2):
            return (0, None)
        c, new = self.combineList(l1.next, l2.next)
        s = l1.val+l2.val+c
        ans = ListNode(s%10)
        ans.next = new
        return (s/10, ans)
                