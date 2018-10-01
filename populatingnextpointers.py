# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return root
        ptr = root
        current_row = collections.deque([ptr])
        while current_row:
            previous = None
            for i in range(len(current_row)):
                node = current_row.pop()
                node.next = previous
                previous = node
                if node.right:
                    current_row.appendleft(node.right)                
                if node.left:
                    current_row.appendleft(node.left)
