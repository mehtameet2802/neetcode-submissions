class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        L = 0 
        R = 0

        while R < len(nums):
            if nums[R] in seen:
                while nums[L] != nums[R]:
                    L+=1
                
                if abs(R-L) <= k:
                    return True
                else:
                    L+=1
            
            seen.add(nums[R])
            R+=1
        
        return False