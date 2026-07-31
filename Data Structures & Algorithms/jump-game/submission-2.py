class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [True]*len(nums)
        n = len(nums)
        i = n-2
        target = n-1

        while i>=0:
            if nums[i] + i < target:
                ans[i] = False
            else:
                target = i
            i-=1
        return ans[0]