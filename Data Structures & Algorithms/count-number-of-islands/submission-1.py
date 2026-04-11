class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid: List[List[str]], row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                return
            
            grid[row][col] = "0"

            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
        
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    result += 1
                    dfs(grid, r, c)
        return result
     

