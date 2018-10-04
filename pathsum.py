class Solution(object):
    def hasPathSum(self, root, sum):
        def check(root, sum):
            if not root:
                return False
            if root.left == None and root.right == None:
                return sum - root.val == 0 
            return check(root.left, sum - root.val) or check(root.right, sum - root.val)
        return check(root, sum)