class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end, num):
            left = start
            right = end

            while left<=right:
                num[left], num[right] = num[right], num[left]
                left += 1
                right -= 1

        k = k%len(nums)    
        reverse(0,len(nums)-1, nums)
        reverse(0,k-1,nums)
        reverse(k,len(nums)-1, nums)
