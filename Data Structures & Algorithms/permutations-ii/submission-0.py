class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        visited = set()

        nums = sorted(nums)

        def helper(res):
            if len(res)==len(nums):
                ans.add(tuple(res.copy()))
            
            for i, num in enumerate(nums):
                if i not in visited:
                    res.append(num)
                    visited.add(i)
                    helper(res)
                    res.pop()
                    visited.remove(i)
            
        helper([])
        return list(ans)