class Solution(object):
    def maxAreaOfIsland(self, grid):
        visited = {}
        maximum = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    island_size = 1 
                    queue = [(i,j)]
                    visited[(i,j)] = True
                    while queue:
                        a,b = queue.pop(0)
                        for c,d in [(a,b+1), (a,b-1), (a+1, b), (a-1, b)]:
                            if 0 <= c < len(grid) and 0 <= d < len(grid[0]) and grid[c][d] == 1 and (c,d) not in visited:
                                visited[(c,d)] = True
                                queue.append((c,d))
                                island_size += 1
                    maximum = island_size if island_size > maximum else maximum
        return maximum 