import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        f_map = Counter(s)

        max_heap = []

        for ele, cnt in f_map.items():
            heapq.heappush(max_heap, (-cnt,ele))
        
        ans = ""
        while max_heap:
            cnt, ele = heapq.heappop(max_heap)

            if len(ans)>0 and ans[-1] == ele:
                if max_heap:
                    cnt2, ele2 = heapq.heappop(max_heap)
                    ans += ele2
                    cnt2+=1

                    if cnt2<0:
                        heapq.heappush(max_heap, (cnt2, ele2))
                    heapq.heappush(max_heap, (cnt,ele))
                else:
                    return ""
            else:
                ans += ele
                cnt+=1
                if cnt < 0:
                    heapq.heappush(max_heap, (cnt, ele))
        
        return ans