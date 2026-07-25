import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = [[float('inf')] * COLS for _ in range(ROWS)]

        min_heap = []
        heapq.heappush(min_heap, (grid[0][0],0,0))


        while min_heap:

            ele = heapq.heappop(min_heap)
            r = ele[1]
            c = ele[2]
            e = ele[0]
            
            res = float('inf')
            for dir in dirs:
                n_r = r+ dir[0]
                n_c = c+ dir[1]

                if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS:
                    continue
                
                ne = max(grid[n_r][n_c], e)

                if ans[n_r][n_c] > e:
                    ans[n_r][n_c] = ne
                else:
                    continue
                
                heapq.heappush(min_heap, (ne,n_r,n_c))
            
        
        return ans[ROWS-1][COLS-1]