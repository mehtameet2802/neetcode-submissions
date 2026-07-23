class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0

        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def helper(r,c):
            nonlocal p

            grid[r][c] = -1
            for dir in dirs:
                n_r = r+dir[0]
                n_c = c+dir[1]

                if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS or grid[n_r][n_c]==0:
                    p+=1
                    continue
                
                if grid[n_r][n_c] == -1:
                    continue
                
                helper(n_r, n_c)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    helper(r,c)

        return p
                
