class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)
        
        ans = 0
        for num in nums:
            if num-1 in seen:
                continue
            
            cur = num
            temp = 0
            while cur in seen:
                temp += 1
                cur += 1
            ans = max(ans, temp)

        return ans