class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[left] > nums[mid]:
                if nums[mid -1] > nums[mid]:
                    return nums[mid]
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]
        
    def findMin(self,nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[left] > nums[mid]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]


[1,2,3,4,5]
[
,1,2,3,4]