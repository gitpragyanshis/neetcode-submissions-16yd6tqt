class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        r_s, r_end = 0, len(matrix)
        row = -1

        while r_s < r_end:
            mid = (r_s + r_end) //2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] < target:
                r_s = mid + 1
            else:
                r_end = mid
        

        c_s, c_e = 0, len(matrix[row])
        while c_s < c_e:
            mid = (c_s + c_e) //2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                c_s = mid + 1
            else:
                c_e = mid
        
        return False
