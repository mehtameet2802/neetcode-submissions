class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1]*len(nums)
        suf_prod = [1]*len(nums)

        for i in range(1,len(nums)):
            pre_prod[i] = pre_prod[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suf_prod[i] = suf_prod[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            pre_prod[i] = pre_prod[i]*suf_prod[i]
        
        return pre_prod

