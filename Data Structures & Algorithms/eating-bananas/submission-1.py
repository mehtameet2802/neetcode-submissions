import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def cal(speed):
            t = 0
            for pile in piles:
                t += math.ceil(pile/speed)
            
            return t <= h

        ans = r

        while l<=r:
            mid = l + (r-l) // 2

            if cal(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
        
