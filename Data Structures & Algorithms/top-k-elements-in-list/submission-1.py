from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = Counter(nums)
        max_heap = []
        ans = []

        for u,v in f_map.items():
            heapq.heappush(max_heap, (-v, u))
        
        while k>0:
            f, num = heapq.heappop(max_heap)
            ans.append(num)
            k-=1
        
        return ans
        
