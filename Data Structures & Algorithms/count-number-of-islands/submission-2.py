class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0" or grid[x][y] == "0":
                return

            grid[x][y] = "0"

            dfs(grid, x + 1, y)
            dfs(grid, x - 1, y)
            dfs(grid, x, y + 1)
            dfs(grid, x, y - 1)
        
        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    result += 1
                    dfs(grid, r, c)
        
        return result