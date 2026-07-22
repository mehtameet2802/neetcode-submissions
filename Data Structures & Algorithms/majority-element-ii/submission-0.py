class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1 = 0
        ele2 = 0
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == ele1:
                cnt1+=1
            elif num == ele2:
                cnt2+=1
            elif cnt1 <= 0:
                ele1 = num
                cnt1 +=1
            elif cnt2 <= 0:
                ele2 = num
                cnt2 += 1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == ele1:
                cnt1+=1
            elif num == ele2:
                cnt2+=1
        
        base = len(nums) // 3
        ans = []

        if cnt1 > base:
            ans.append(ele1)
        
        if cnt2 > base:
            ans.append(ele2)

        return ans 