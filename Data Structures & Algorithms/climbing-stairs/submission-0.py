class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        cnt = 0
        mem = {}

        def helper(i):
            if i in mem:
                return mem[i]

            if i > n:
                return 0

            if i == n:
                return 1

            ans = helper(i+1) + helper(i+2)
            mem[i] = ans

            return ans

        return helper(0) 
            
