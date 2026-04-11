class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.binary_search_row(matrix, target)
        if row < 0 or row >= len(matrix):
            return False
        col = self.binary_search_col(matrix[row], target)

        return True if col < len(matrix[row]) and matrix[row][col] == target else False
    
    def binary_search_row(self, matrix: List[List[int]], target: int) -> int:
        start, end = 0, len(matrix)

        while start < end:
            mid = (start + end) //2

            if matrix[mid][-1] < target:
                start = mid + 1
            else:
                end = mid
        return start
    
    def binary_search_col(self, arr: List[int], target: int) -> int:
        start, end = 0, len(arr)

        while start < end:
            mid = (start + end) //2

            if arr[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start