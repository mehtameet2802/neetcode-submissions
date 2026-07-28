class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        f = 0
        e = len(s)-1

        mem = {}

        def helper(l,r):
            if (l,r) in mem:
                return mem[(l,r)]

            if l>r:
                return 0
            
            if l==r:
                return 1
            
            if s[l] == s[r]:
                ans = 2 + helper(l+1,r-1)
            else:
                ans = max(helper(l+1,r), helper(l,r-1))

            mem[(l,r)] = ans

            return ans
        
        return helper(f,e)

    