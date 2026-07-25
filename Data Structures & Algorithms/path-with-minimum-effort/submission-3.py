import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        ans = [[float('inf')] * COLS for _ in range(ROWS)]
        ans[0][0] = 0


        min_heap = []
        heapq.heappush(min_heap,(0,0,0))

        while min_heap:

            ele = heapq.heappop(min_heap)
            w = ele[0]
            r = ele[1]
            c = ele[2]

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                    continue

                diff = abs(heights[nr][nc] - heights[r][c])
                nw = max(diff, w)

                if ans[nr][nc] > nw:
                    ans[nr][nc] = nw
                else:
                    continue
                
                heapq.heappush(min_heap, (nw,nr,nc))
            
        return ans[ROWS-1][COLS-1]


