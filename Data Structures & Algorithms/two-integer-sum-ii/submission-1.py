class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i_map = {}

        # for i, num in enumerate(numbers):
        #     find = target - num
        #     if find in i_map and find!=num:
        #         return [i_map[find], i+1]
        #     else:
        #         i_map[num] = i+1
        
        # return []

        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right -= 1
            elif numbers[left]+numbers[right]<target:
                left += 1
            else:
                return [left+1, right+1]
        
        return []