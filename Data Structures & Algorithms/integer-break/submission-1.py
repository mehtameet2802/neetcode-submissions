class Solution:
    def integerBreak(self, n: int) -> int:

        ans = 0
        mem = {}
        
        def helper(i, cur_sum):

            if (i,cur_sum) in mem:
                return mem[(i,cur_sum)]

            if cur_sum == n:
                return 1

            if i>=n or cur_sum>n:
                return 0
            
            a1 = i*helper(i, cur_sum+i)
            a2 = helper(i+1, cur_sum)

            mem[(i,cur_sum)] = max(a1, a2)
            return mem[(i,cur_sum)]

        return helper(1,0)

