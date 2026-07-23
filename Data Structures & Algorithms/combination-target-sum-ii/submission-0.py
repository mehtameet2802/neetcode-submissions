class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        res = []

        def helper(i, sum):            
            if sum == target:
                ans.append(res.copy())
                return
            
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                
                if sum+candidates[j] > target:
                    continue
                
                res.append(candidates[j])
                helper(j+1, sum+candidates[j])
                res.pop()

        
        helper(0, 0)
        return ans