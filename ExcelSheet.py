class Solution(object):
    def convertToTitle(self, n):
        result = ""
        while n:
            remainder = (n-1) % 26 
            n = (n-1)/26
            result = (chr(remainder + 65)) + result
        return result
    
    
