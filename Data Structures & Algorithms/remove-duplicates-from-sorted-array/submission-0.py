class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        read = 0
        write = 0

        while write<len(nums):
            while read<len(nums) and nums[read] == nums[write]:
                read += 1
            
            if read<len(nums):
                nums[write+1] = nums[read]
                cnt += 1
            
            write+=1
        
        return cnt
