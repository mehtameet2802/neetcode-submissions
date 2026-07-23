import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap,-stone)
        
        while len(max_heap)>1:
            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)

            if s1 == s2:
                continue
            
            new_s = abs(s1-s2)
            heapq.heappush(max_heap, -new_s)
        
        if not max_heap:
            return 0
        
        return -max_heap[0]


             
