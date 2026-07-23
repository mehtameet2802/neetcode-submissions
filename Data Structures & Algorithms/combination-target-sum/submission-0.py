class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        res = []
        
        def helper(i, sum):
            if i>=len(nums):
                return
            
            if sum == target:
                ans.append(res.copy())

            for j in range(i, len(nums)):
                if sum + nums[j] > target:
                    continue
                
                res.append(nums[j])
                helper(j, sum+nums[j])
                res.pop()
            
        helper(0, 0)
        return ans