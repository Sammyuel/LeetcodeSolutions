class Solution(object):
    def updateMatrix(self, matrix):
        q, m, n = [], len(matrix), len(matrix[0])
        seen = {}
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
        while q:
            i,j = q.pop(0)
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > 0:
                    if (r,c) not in seen or seen[(r,c)] > z:
                        seen[(r,c)] = z
                        matrix[r][c] = z
                        q.append((r, c))
        return matrix