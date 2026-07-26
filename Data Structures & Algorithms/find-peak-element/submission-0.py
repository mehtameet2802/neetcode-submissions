class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return 0
        
        for i in range(n):
            if i==0 and nums[i]>nums[i+1] or i==n-1 and nums[i]>nums[i-1]:
                return i
            
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
        
        return 0