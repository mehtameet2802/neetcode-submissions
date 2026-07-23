import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            heapq.heappush(self.min_heap,num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        while len(self.min_heap)>self.k:
            heapq.heappop(self.min_heap)
        
        # ele = heapq.heappop(self.min_heap)
        # heapq.heappush(self.min_heap, ele)
        return self.min_heap[0]
