class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        visited = set()

        def helper(i):
            if len(res) == len(nums):
                ans.append(res.copy())
                return
            
            for j in range(0,len(nums)):
                if nums[j] in visited:
                    continue
                
                visited.add(nums[j])
                res.append(nums[j])
                helper(j+1)
                res.pop()
                visited.remove(nums[j])
        
        helper(0)
        return ans
