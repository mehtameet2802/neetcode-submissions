class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        min_l = len(strs[0])
        min_w = strs[0]

        for word in strs[1:]:
            for i, ch in enumerate(min_w):
                if len(word)<=i or ch != word[i]:
                    min_l = min(min_l, i)
                    break

        return min_w[:min_l]