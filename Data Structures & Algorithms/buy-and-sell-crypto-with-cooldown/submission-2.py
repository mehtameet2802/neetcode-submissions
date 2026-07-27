class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mem = {}

        def helper(i,holding):
            if (i,holding) in mem:
                return mem[(i,holding)]

            if i>=len(prices):
                return 0
            
            if not holding:
                p1 = -prices[i] + helper(i+1, True)
            else:
                p1 = prices[i] + helper(i+2,False)
            
            p2 = helper(i+1, holding)

            cur_p = max(p1,p2)
            mem[(i,holding)] = cur_p
            return cur_p
        
        return helper(0,False)

