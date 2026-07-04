class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        
        result = set()


        for i, num in enumerate(nums):
            i_map = set()
            for j, num1 in enumerate(nums[i+1:]):
                target = 0 - num - num1
                if target in i_map:
                    result.add(tuple(sorted([num, num1, target])))
                else:
                    i_map.add(num1)
        
        return list(result)