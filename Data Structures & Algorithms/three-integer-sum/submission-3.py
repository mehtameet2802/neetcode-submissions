class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        
        # result = set()
        # nums = sorted(nums)


        # for i, num in enumerate(nums):
        #     i_map = set()
        #     for j, num1 in enumerate(nums[i+1:]):
        #         target = 0 - num - num1
        #         if target in i_map:
        #             result.add((num, target, num1))
        #         else:
        #             i_map.add(num1)
        
        # return list(result)

        result = set()
        nums = sorted(nums)

        for i, num in enumerate(nums):
            left = i+1
            right = len(nums)-1
            target = 0
            while left<right:
                if nums[left]+nums[right]>target-num:
                    right -= 1
                elif nums[left]+nums[right]<target-num:
                    left += 1
                elif nums[left]+nums[right] == target-num:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        return list(result)
