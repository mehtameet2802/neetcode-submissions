class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [0,-1], [-1,0], [1,0]]
        cnt = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def helper(r,c):
            grid[r][c] = -1
            area = 0
            for dir in dirs:
                n_r = dir[0] + r
                n_c = dir[1] + c

                if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS or grid[n_r][n_c]==0 or grid[n_r][n_c] == -1:
                    continue
                
                area += helper(n_r, n_c)
            return area+1
        
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    ans = max(ans, helper(i,j))
        
        return ans
            