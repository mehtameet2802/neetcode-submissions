from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        t = 0
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh:
            
            size = len(queue)
            for _ in range(size):
                ele = queue.popleft()
                r = ele[0]
                c = ele[1]
                for dir in dirs:
                    n_r = r + dir[0]
                    n_c = c + dir[1]

                    if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS or grid[n_r][n_c] != 1 :
                        continue
                    
                    grid[n_r][n_c] = 2
                    fresh -= 1
                    queue.append((n_r,n_c))
            
            t += 1

        return t if fresh==0 else -1
