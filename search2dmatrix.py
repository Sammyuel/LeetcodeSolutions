class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) / 2
            if target < matrix[mid][0]:
                right = mid - 1 
            elif target > matrix[mid][-1]:
                left = mid + 1 
            else:
                for number in matrix[mid]:
                    if number == target:
                        return True
                return False
        return False

finding a pattern for 2d matrix 
