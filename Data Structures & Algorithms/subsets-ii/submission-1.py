class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []

        nums = sorted(nums)

        def helper(i):
            ans.append(res.copy())
            
            for j in range(i, len(nums)):
                if j>i and nums[j-1]==nums[j]:
                    continue
                
                res.append(nums[j])
                helper(j+1)
                res.pop()
            
        helper(0)
        return ans