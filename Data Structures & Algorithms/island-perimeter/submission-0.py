class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()

        def dfs(grid: List[List[int]], r: int, c: int) -> int:
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))

            p = dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)

            return p

        row = len(grid)
        column = len(grid[0])
        result = 0

        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    return dfs(grid, r, c)
        
        return 0
        

        



    