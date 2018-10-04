class Solution(object):
    def maxSubArray(self, nums):
        total = nums[0]
        current_total = 0
        for i, num in enumerate(nums):
            current_total += num
            if current_total > total:
                total = current_total
            if current_total <= 0:
                current_total = 0 
        return total 