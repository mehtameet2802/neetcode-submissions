class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        res = []

        nums = sorted(nums)

        def helper(i):
            if len(res) == len(nums):
                ans.append(res.copy())
                return
            
            for j in range(len(nums)):
                if j>0 and nums[j] == nums[j-1] and j-1 not in visited:
                    continue
                
                if j not in visited:
                    res.append(nums[j])
                    visited.add(j)
                    helper(j+1)
                    res.pop()
                    visited.remove(j)
            
        helper(0)
        return ans