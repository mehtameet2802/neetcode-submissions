import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x,y in points:
            dist = pow(pow(x,2) + pow(y,2),0.5)
            heapq.heappush(max_heap, (-dist,x,y))
        
        while len(max_heap)>k:
            heapq.heappop(max_heap)
        
        ans = []
        for d,x,y in max_heap:
            ans.append([x,y])
        
        return ans