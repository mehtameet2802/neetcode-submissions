class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = 0
        l2 = 0

        ans = ""

        while l1<len(word1) and l2<len(word2):
            ans = ans+word1[l1]+word2[l2]
            l1 += 1
            l2 += 1

        if l1<len(word1):
            ans += word1[l1:]
        
        if l2<len(word2):
            ans += word2[l2:]
        
        return ans

