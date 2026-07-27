class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        def helper(r,c):

            for i in range(ROWS):
                if matrix[i][c] != 0:
                    matrix[i][c] = "#"

            for i in range(COLS):
                if matrix[r][i] !=0:
                    matrix[r][i] = "#"

        for i in range(ROWS):
            for j in range(COLS):
                
                if matrix[i][j] == 0:
                    matrix[i][j] = "#"
                    helper(i,j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
