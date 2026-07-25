from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = defaultdict(list)
        c = defaultdict(list)

        ROWS = len(grid)
        COLS = len(grid[0])
    
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    r[i].append((i,j))
                    c[j].append((i,j))
        
        cnt = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1 and (len(r[i])>1 or len(c[j])>1):
                    cnt+=1

        return cnt