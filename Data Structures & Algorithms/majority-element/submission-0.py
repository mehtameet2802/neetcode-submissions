class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        cnt = 1
        i = 1
        while i<len(nums):
            if nums[i] == ele:
                cnt+=1
            else:
                cnt -= 1
                if cnt<=0:
                    ele = nums[i]
            i+=1

        return ele