class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if nums[r] >= nums[l]:
            return nums[l]

        while l<=r:
            mid = l + (r-l)//2

            if nums[l]<=nums[mid] and nums[r]<nums[mid]:
                l = mid+1
            elif mid>0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[r] > nums[mid]:
                r = mid-1
            else:
                l = mid + 1
