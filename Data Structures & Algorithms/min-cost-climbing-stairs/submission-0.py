class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem = {}

        def helper(i):
            if i in mem:
                return mem[i]

            if i >= len(cost):
                return 0
            
            l = helper(i+1)
            r = helper(i+2)

            ans = min(l,r) + cost[i]
            mem[i] = ans

            return ans
        
        return min(helper(0), helper(1))
            
