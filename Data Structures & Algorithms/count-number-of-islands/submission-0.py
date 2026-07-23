class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dirs = [[0,1], [0,-1], [-1,0], [1,0]]
        cnt = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def helper(r,c):
            grid[r][c] = "-1"

            for dir in dirs:
                n_r = dir[0] + r
                n_c = dir[1] + c

                if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS or grid[n_r][n_c]=="0" or grid[n_r][n_c] == "-1":
                    continue
                
                helper(n_r, n_c)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    helper(i,j)
                    cnt+=1
        
        return cnt
            