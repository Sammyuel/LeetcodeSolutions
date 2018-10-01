class Solution(object):
    def islandPerimeter(self, grid):
        visited = {}
        perimeter = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    q = [(i,j)]
                    while q:
                        a,b = q.pop(0)
                        visited[(a,b)] = True
                        for c,d in [(a, b+1), (a, b-1), (a+1, b), (a-1, b)]:
                            if not 0 <= c < len(grid) or not 0 <= d < len(grid[0]) or grid[c][d] == 0:
                                perimeter +=1 
                            elif grid[c][d] == 1 and (c,d) not in visited:
                                q.append((c,d))
                                visited[(c,d)] = True
                    return perimeter