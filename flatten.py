# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        def traverse(node, previous):
            if previous:
                previous.left = node
            traverse(node.left, node)
            traverse(node.right, node)
        traverse(root, None)
        ptr = root
        while ptr:
            ptr.right = ptr.left
            ptr.left = None
            ptr = ptr.right
        
        
            