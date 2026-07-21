class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
            
        l = 0
        r = x // 2

        while l<=r:
            mid = l + (r-l) // 2
            cal = mid * mid

            if cal == x:
                return mid
            elif cal < x:
                l = mid + 1
            else: 
                r = mid - 1
        
        return r
            