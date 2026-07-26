class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans = []
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        # def helper(r,c,a):

        #     state = False
        #     grid[r][c] = -1
        #     for dr, dc in dirs:
        #         nr = r+dr
        #         nc = c+dc

        #         if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]!=1:
        #             continue

        #         if r==0 or nr==0 or r==ROWS-1 or c==0 or nc==0 or c==COLS-1:
        #             state = state or True
                
                
        #         grid[nr][nc] = -1
        #         a1, nstate = helper(nr,nc,0)
        #         state = state or nstate
        #         a += a1
            
        #     return a, state


    
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == 1:
        #             a, state = helper(i,j,0)
        #             ans.append((a,state))
        
        # total = 0
        # for ele in ans:
        #     if not ele[1]:
        #         total += ele[0]
        
        # return total

        def helper(r,c):

            grid[r][c] = -1

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]!=1:
                    continue
                
                helper(nr,nc)

        for c in range(COLS):
            if grid[0][c] == 1:
                helper(0,c)
        
        for r in range(1, ROWS):
            if grid[r][COLS-1] == 1:
                helper(r, COLS-1)
        
        for c in range(COLS-1,-1,-1):
            if grid[ROWS-1][c] == 1:
                helper(ROWS-1,c)
        
        for r in range(ROWS-1,-1,-1):
            if grid[r][0] == 1:
                helper(r,0)
        
        cnt = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    cnt+=1
        
        return cnt

        
