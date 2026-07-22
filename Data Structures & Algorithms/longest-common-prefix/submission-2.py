class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        s = strs[0]
        if s == "":
            return ""

        for i in range(1,len(strs)):
            s1 = ""
            if strs[i] == "":
                return ""
            length = min(len(s),len(strs[i]))
            for j in range(length):
                if s[j] == strs[i][j]:
                    s1 += s[j]
                else:
                    break
            if len(s1)<len(s):
                s = s1
        return s
            


