class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            val1 = nums[i]
            for j in range(i+1, len(nums)):
                val2 = nums[j]

                find = target - val1 - val2
                left = j+1
                right = len(nums)-1

                while left<right:
                    if nums[left] + nums[right] < find:
                        left += 1
                    elif nums[left] + nums[right] > find:
                        right -= 1
                    else:
                        result.add((val1, val2, nums[left], nums[right]))
                        left += 1
                        right -=1

        return list(result)
