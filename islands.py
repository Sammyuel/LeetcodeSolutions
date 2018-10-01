class Solution(object):
    def numIslands(self, grid):
        result = 0
        islands = set([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    result += 1
                    q = collections.deque()
                    q.append((i,j))
                    while q:
                        (a,b) = q.pop()
                        grid[a][b] = 2
                        for (di, dj) in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                            if 0 <= (a + di) < len(grid) and 0 <= (b + dj) < len(grid[i]) and grid[a+di][b+dj] == '1':
                                q.append((a+di,b+dj))

        return result
                
                
                        