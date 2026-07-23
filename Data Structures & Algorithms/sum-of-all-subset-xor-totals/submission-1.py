class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def helper(i,cur):
            nonlocal ans

            if i>=len(nums):
                ans += cur
                return

            helper(i+1, cur^nums[i])
            helper(i+1, cur)

        helper(0, 0)
        return ans