class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = set()
        
        nums = sorted(nums)

        def helper(i):
            if i>=len(nums):
                ans.add(tuple(res))
                return
            
            res.append(nums[i])
            helper(i+1)
            res.pop()
            helper(i+1)
            
        helper(0)
        return list(ans)