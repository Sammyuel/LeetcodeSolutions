class Solution(object):
    def levelOrderBottom(self, root):
        result = []
        if not root:
            return result
        q = [root]
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        result[:] = result[::-1]
        return result