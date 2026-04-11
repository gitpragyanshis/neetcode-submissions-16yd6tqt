class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        s_box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                curr = board[r][c]

                if curr == ".":
                    continue
                
                s_i = r // 3 * 3 + c // 3 
                if curr in row[r] or curr in column[c] or curr in s_box[s_i]:
                    return False
                row[r].add(curr)
                column[c].add(curr)
                s_box[s_i].add(curr)
        
        return True
