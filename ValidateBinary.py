# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, min_limit = None, max_limit = None):
        if root == None:
            return True
        if max_limit != None and root.val >= max_limit:
            return False
        if min_limit != None and root.val <= min_limit:
            return False
        left = self.isValidBST(root.left, min_limit, root.val)
        right = self.isValidBST(root.right, root.val, max_limit)
        return left and right
        