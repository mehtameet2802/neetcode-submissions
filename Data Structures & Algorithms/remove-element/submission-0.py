class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # rp =0
        # while rp<len(nums):
        #     if nums[rp]!=val:
        #         rp+=1
        #         continue
            
        #     wp = rp+1

        #     while wp<len(nums) and nums[wp] == val:
        #         wp+=1

            
        #     while nums[rp] == val:
        #         nums[rp], nums[wp] = nums[wp], nums[rp]
        #         rp+=1
        #         wp+=1
            
        #     rp = wp
        
        # print(nums)
        
        wp = 0
        for num in nums:
            if num == val:
                continue
            
            nums[wp] = num
            wp+=1
        
        return wp

