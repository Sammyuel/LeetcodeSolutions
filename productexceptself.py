class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        result = []
        for num in nums:
            result.append(product)
            product *= num
        product = 1 
        for i in range(len(nums)):
            result[-(i+1)] *= product
            product *= nums[-(i+1)]
        return result