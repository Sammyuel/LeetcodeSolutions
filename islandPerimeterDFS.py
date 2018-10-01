class Solution(object):
    def islandPerimeter(self, grid):
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.helper(grid, i, j, visited)
    
        return 0

    def helper(self, grid, i, j, visited):
        if (i, j) in visited:
            return 0
        
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0:
            return 1
        
        visited.add((i, j))
        return self.helper(grid, i + 1, j, visited) + self.helper(grid, i - 1, j, visited) + self.helper(grid, i, j + 1, visited) + self.helper(grid, i, j - 1, visited)