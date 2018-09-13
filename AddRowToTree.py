# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        if root == None:
            return 
        newLeft = TreeNode(v)
        newRight = TreeNode(v)
        if d == 1:
            newLeft.left = root
            return newLeft
        if d == 2:
            leftNode = root.left
            rightNode = root.right
            root.left = newLeft
            root.right = newRight
            newLeft.left = leftNode
            newRight.right = rightNode
            return root
        self.addOneRow(root.left, v, d-1)
        self.addOneRow(root.right, v, d-1)
        return root
        