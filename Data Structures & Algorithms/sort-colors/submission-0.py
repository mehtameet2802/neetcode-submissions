class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for num in nums:
            if num == 0:
                cnt1 += 1
            elif num == 1:
                cnt2 += 1
            else:
                cnt3 += 1
        
        i = 0
        while cnt1>0:
            nums[i] = 0
            i += 1
            cnt1 -= 1

        while cnt2>0:
            nums[i] = 1
            i += 1
            cnt2 -= 1
        
        while cnt3 > 0:
            nums[i] = 2
            i += 1
            cnt3 -= 1

        