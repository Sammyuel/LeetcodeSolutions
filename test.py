class Solution():
    def permute(self, nums):
        self.res = []
        def dfs(nums, path):
            if not nums:
                self.res.append(path)
                # return # backtracking
            for i in xrange(len(nums)):
                dfs(nums[:i]+nums[i+1:] or [], path+[nums[i]])
        dfs(nums, [])
        return self.res


class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)