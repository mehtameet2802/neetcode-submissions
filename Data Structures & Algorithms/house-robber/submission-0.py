class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mem = {}

        def helper(i):
            if i in mem:
                return mem[i]
            
            if i >= len(nums):
                return 0
            
            o1 = helper(i+2) + nums[i]
            o2 = helper(i+1)

            ans = max(o1,o2)
            mem[i] = ans

            return ans
        
        return helper(0)
