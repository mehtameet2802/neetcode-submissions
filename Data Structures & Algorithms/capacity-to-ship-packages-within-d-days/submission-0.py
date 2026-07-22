class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def cal(cap):
            n_days = 1
            utilized = 0
            for weight in weights:
                if utilized + weight > cap:
                    n_days += 1
                    utilized = weight
                else:
                    utilized += weight
            
            return n_days<=days

        ans = r
        
        while l<=r:
            mid = l+(r-l)//2

            if cal(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans