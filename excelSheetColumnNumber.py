class Solution():
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
            
        col = 0 
        for l in s:
            col = 26*col + ord(l) - 64
        
        return col
    