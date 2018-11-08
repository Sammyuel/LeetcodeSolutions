class Solution(object):
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        
        # reverse + transpose
        
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        

Test = 
	[
	[1,2,3,4,5],
	[6,7,8,9,10],
	[11,12,13,14,15],
	[16,17,18,19,20],
	[21,22,23,24,25],
	[26,27,28,29,30]
	]

Reverse = 
	[
	[26,27,28,29,30],
	[21,22,23,24,25],
	[16,17,18,19,20],
	[11,12,13,14,15],
	[6,7,8,9,10],
	[1,2,3,4,5]
	]