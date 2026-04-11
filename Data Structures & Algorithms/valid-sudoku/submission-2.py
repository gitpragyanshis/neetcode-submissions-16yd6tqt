class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(len(board[0]))]
        col = [set() for _ in range(len(board[0]))]
        sub_grid = [set() for _ in range(9)]


        for ri in range(len(board)):
            for ci in range(len(board[ri])):
                value = board[ri][ci]
                if value == ".":
                    continue
                
                sub_grid_index = (ri // 3) * 3 + (ci // 3)

                if value in row[ri] or value in col[ci] or value in sub_grid[sub_grid_index]:
                    return False

                row[ri].add(value)
                col[ci].add(value)
                sub_grid[sub_grid_index].add(value)

        return True