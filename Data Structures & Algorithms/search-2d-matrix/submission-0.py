class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        n = ROWS*COLS

        l = 0
        r = n-1

        while l<=r:
            mid = l + (r-l) // 2

            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid+1
            else:
                r = mid-1
            
        return False
        