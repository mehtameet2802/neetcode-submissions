class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        res = []
        def cal(arr):
            nonlocal ans

            x = 0
            for num in arr:
                x = x^num
            ans += x
        

        def helper(i):
            if i>=len(nums):
                cal(res)
                return
            
            res.append(nums[i])
            helper(i+1)
            res.pop()
            helper(i+1)

        helper(0)
        return ans