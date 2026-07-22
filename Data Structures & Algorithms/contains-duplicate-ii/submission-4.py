class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        L = 0 
        R = 0

        while R < len(nums):
            if nums[R] in seen:
                if abs(R-seen[nums[R]]) <= k:
                    return True
                else:
                    seen[nums[R]] = L
            
            seen[nums[R]] = R
            R+=1
        
        return False