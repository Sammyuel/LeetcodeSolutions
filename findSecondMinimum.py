class Solution(object):
    def findSecondMinimumValue(self, root):
        self.res = None
        def traverse(node):
            if not node:
                return
            if not self.res and node.val != root.val:
                self.res = node.val
            elif root.val < node.val < self.res:
                self.res = node.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return -1 if not self.res else self.res