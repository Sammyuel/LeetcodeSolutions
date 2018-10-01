# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def path(self, root, k):
        if not root:
            return []
        if root == k:
            return [root]
        res = self.path(root.left, k)
        if res:
            return [root] + res
        res = self.path(root.right, k)
        if res:
            return [root] + res
        return []
    
    def lowestCommonAncestor(self, root, p, q):
        p_path = self.path(root, q)
        q_path = self.path(root, p)
        min_length = min(len(p_path), len(q_path))
        p_path = p_path[0:min_length ]
        q_path = q_path[0:min_length ]
        p_node = p_path.pop(-1)
        q_node = q_path.pop(-1)
        
        while p_path and q_path and p_node != q_node:
            p_node = p_path.pop(-1)
            q_node = q_path.pop(-1)
        return q_node
    
