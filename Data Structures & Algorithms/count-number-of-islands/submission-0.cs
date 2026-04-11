public class Solution {
    public int NumIslands(char[][] grid) {
        int result = 0;

        for(int i = 0; i < grid.Length; i++)
        {
            for(int j = 0; j < grid[i].Length; j++)
            {
                if(grid[i][j] == '1')
                {
                    result++;
                    Search(grid, i, j);
                }
            }
        }

        return result;
    }
    
    public void Search(char[][] grid, int row, int column)
    {
        if(row < 0 || row >= grid.Length || column < 0 || column >= grid[0].Length || grid[row][column] == '0')
        {
            return;
        }

        grid[row][column] = '0';
        Search(grid, row + 1, column);
        Search(grid, row -1, column);
        Search(grid, row, column + 1);
        Search(grid, row, column - 1);
    }

}
