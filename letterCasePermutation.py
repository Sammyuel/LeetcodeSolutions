class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        s = list(S)
        def dfs(index, path):
            if index == len(S):
                res.append(path)
                return 
            dfs(index+1, path + s[index])
            if s[index].isalpha():
                dfs(index+1, path +s[index].swapcase())
        dfs(0, "")
        return res
        