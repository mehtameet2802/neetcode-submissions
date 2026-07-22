from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = deque([])
        cnt = 0

        for num in arr:
            if cnt<k:
                ans.append(num)
                cnt+=1
                continue
            
            diff1 = abs(ans[0]-x)
            diff2 = abs(num-x)

            if diff1<diff2 or diff1 == diff2 and ans[0]<num:
                continue
            else:
                ans.popleft()
                ans.append(num)
        
        return list(ans)
            