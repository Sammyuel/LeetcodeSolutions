class Solution(object):
    def isSubtree(self, s, t):
        if s == None:
            return False
        if s.val == t.val and self.matchTree(s,t):
            return True
        left = self.isSubtree(s.left,t)
        right = self.isSubtree(s.right,t)
        return left or right
        
    def matchTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        left = self.matchTree(s.left,t.left)
        right = self.matchTree(s.right,t.right)
        return left and right