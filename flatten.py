class Solution(object):
    def flatten(self, root):
        self.previous = None
        def traverse(node):
            if not node:
                return 
            if self.previous:
                self.previous.left = node
            self.previous = node
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        ptr = root
        while ptr:
            ptr.right = ptr.left
            ptr.left = None
            ptr = ptr.right