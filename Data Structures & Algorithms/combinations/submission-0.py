class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        res = []

        def helper(i):
            if len(res) == k:
                ans.append(res.copy())
                return
            
            for j in range(i, n+1):

                res.append(j)
                helper(j+1)
                res.pop()
            
        helper(1)
        return ans