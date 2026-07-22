from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        pre_map = defaultdict(int)

        pre = [0]*len(nums)
        pre[0] = nums[0]


        for i in range(1,len(nums)):
            pre[i] = pre[i-1] + nums[i]

        pre_map[0] = 1

        ans = 0
        for prefix in pre:
            ans += pre_map[prefix-k]
            pre_map[prefix] += 1
        
        return ans
