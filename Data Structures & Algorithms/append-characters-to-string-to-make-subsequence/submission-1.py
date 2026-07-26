class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1 = 0
        p2 = 0

        while p1<len(t) and p2<len(s):
            if t[p1] == s[p2]:
                p1+=1
                p2+=1
            else:
                p2+=1
        
        return len(t)-p1
        
