class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []

        def helper(i):
            nonlocal ans
            nonlocal res

            if i>=len(nums):
                ans.append(res.copy())
                return

            res.append(nums[i])
            helper(i+1)
            res.pop()
            helper(i+1)

        helper(0)
        return ans