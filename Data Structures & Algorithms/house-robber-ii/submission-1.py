class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mem = {}

        if len(nums) == 1:
            return nums[0]

        def helper(i, start):
            if (i,start) in mem:
                return mem[(i,start)]

            if i>=len(nums):
                return 0

            if i == len(nums)-1:
                if start == 0:
                    return 0

            o1 = helper(i+2, start) + nums[i]
            o2 = helper(i+1, start)

            ans = max(o1, o2)
            mem[(i,start)] = ans
            return ans
        
        return max(helper(0, 0),helper(1, 1))
            
