public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var set = new Dictionary<(int, int), HashSet<char>>();
        var row = new Dictionary<int, HashSet<char>>();
        var column = new Dictionary<int, HashSet<char>>();
        for (int i = 0; i < board.Length; i++) {
            for (int j = 0; j < board[0].Length; j++) {
                if (board[i][j] == '.') continue; // Skip empty cells

                if (!row.ContainsKey(i)) {
                    row.Add(i, new HashSet<char> { board[i][j] });
                } else {
                    if (row[i].Contains(board[i][j])) {
                        return false;
                    } else {
                        row[i].Add(board[i][j]);
                    }
                }

                if (!column.ContainsKey(j)) { // Use 'j' as the key for columns
                    column.Add(j, new HashSet<char> { board[i][j] });
                } else {
                    if (column[j].Contains(board[i][j])) {
                        return false;
                    } else {
                        column[j].Add(board[i][j]);
                    }
                }

                var x = i / 3;
                var y = j / 3;

                if (!set.ContainsKey((x, y))) {
                    set.Add((x, y), new HashSet<char> { board[i][j] });
                } else {
                    if (set[(x, y)].Contains(board[i][j])) {
                        return false;
                    } else {
                        set[(x, y)].Add(board[i][j]);
                    }
                }
            }
        }

        return true;
    }
}
