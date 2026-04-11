class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                
                sub_box = (r // 3) * 3 + c // 3
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sub[sub_box]:
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sub[sub_box].add(board[r][c])
        
        return True

