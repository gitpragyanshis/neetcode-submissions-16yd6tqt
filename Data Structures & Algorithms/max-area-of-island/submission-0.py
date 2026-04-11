class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, x, y, area):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
                return 0

        def dfs(grid, x, y):
            if (x < 0 
            or x >= len(grid)
            or y < 0
            or y >= len(grid[0])
            or grid[x][y] != 1):
                return 0
            
            grid[x][y] = 0
            count = 1
            count += dfs(grid, x + 1, y)
            count += dfs(grid, x - 1, y)
            count += dfs(grid, x, y + 1)
            count += dfs(grid, x, y - 1)
            return count
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(grid, i, j))
        
        return max_area
