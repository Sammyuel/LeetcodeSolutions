class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root.left, root.right)