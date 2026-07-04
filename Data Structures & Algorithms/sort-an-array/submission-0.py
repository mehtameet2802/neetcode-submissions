class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            ans = []

            i = 0
            j = 0
            while i<len(left) or j<len(right):
                if i<len(left) and j>=len(right):
                    ans.append(left[i])
                    i += 1
                elif j<len(right) and i>=len(left):
                    ans.append(right[j])
                    j += 1
                else:
                    if left[i] <= right[j]:
                        ans.append(left[i])
                        i += 1
                    else:
                        ans.append(right[j])
                        j += 1
            
            return ans


        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums)//2

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)

        return mergeSort(nums)
