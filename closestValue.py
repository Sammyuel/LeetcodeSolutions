class Solution(object):
    def closestValue(self, root, target):
        self.difference = abs(root.val - target)
        self.result = root
        def traverse(node):
            if not node:
                return 
            value = node.val - target
            if abs(value) < self.difference:
                self.difference = abs(value)
                self.result = node
            if value < 0: 
                traverse(node.right)
            elif value > 0:
                traverse(node.left)
        traverse(root)
        return self.result.val

class Solution(object):
    def closestValue(self, root, target):
        r = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                r = root.val
            root = root.left if target < root.val else root.right
        return r