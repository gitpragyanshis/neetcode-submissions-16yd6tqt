class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            l = len(q)

            for i in range(l):
                row, col = q.popleft()

                for ndr, ndc in [(0, 1), (0 , -1), (1, 0), (-1, 0)]:
                    nr, nc = row + ndr, col + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1

        return -1 if fresh > 0 else time
        