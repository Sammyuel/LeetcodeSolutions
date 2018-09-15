class Solution(object):
    def reverseWords(self,l):    
        index = 0
        for i in range(len(l)/2):
            l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
        
        for i in range(len(l) + 1):
            if i == len(l) or l[i] == " ":
                k = 0 
                for j in range(index, (i+index)/2 ):
                    l[j], l[i-k-1] = l[i-k-1], l[j]
                    k+= 1
                k = 0 
                index = i + 1
        
    

