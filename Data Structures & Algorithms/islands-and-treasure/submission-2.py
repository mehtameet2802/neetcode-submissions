from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        INF = pow(2,31) - 1
        visited = set()

        def helper():
            while queue:

                size = len(queue)

                for _ in range(size):

                    ele = queue.popleft()
                    
                    r = ele[0]
                    c = ele[1]
                    visited.add((r,c))

                    for dir in dirs:
                        n_r = r + dir[0]
                        n_c = c + dir[1]

                        if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS or grid[n_r][n_c]==0 or grid[n_r][n_c]==-1:
                            continue
                        
                        if (n_r,n_c) not in visited:
                            new_d = grid[r][c] + 1
                            cur_d = grid[n_r][n_c] 
                            grid[n_r][n_c] = min(new_d, cur_d)
                            queue.append((n_r,n_c))
                            visited.add((n_r,n_c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        helper()
        

         

