public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        var start = 0;
        var end = matrix.Length - 1;

        while (start <= end) {
            var mid = (start + end) / 2;
            var midValue = matrix[mid][0];

            if (target < midValue) {
                end = mid - 1;
            } else if (target >= midValue && target <= matrix[mid][matrix[mid].Length - 1]) {
                start = mid;
                break;
            } else {
                start = mid + 1;
            }
        }

        if (start >= matrix.Length) {
            return false;
        }

        var rstart = 0;
        var rend = matrix[start].Length - 1;
        while (rstart <= rend) {
            var mid = (rstart + rend) / 2;
            var midValue = matrix[start][mid];

            if (midValue == target) {
                return true;
            }

            if (target < midValue) {
                rend = mid - 1;
            } else {
                rstart = mid + 1;
            }
        }

        return false;
    }

}
