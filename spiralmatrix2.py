class Solution(object):
    def generateMatrix(self, n):
        if n < 1:
            return []
        if n == 1:
            return [[1]]
        matrix = []
        for i in range(n):
            row = [False] * n 
            matrix.append(row)
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        count = 0
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                count += 1
                matrix[top][i] = count
            for j in range(top + 1, bottom + 1):
                count += 1
                matrix[j][right] = count 
            for i in reversed(range(left , right)):
                count += 1
                matrix[bottom][i] = count
            for i in reversed(range(top + 1, bottom)):
                count += 1
                matrix[i][left] = count

            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix