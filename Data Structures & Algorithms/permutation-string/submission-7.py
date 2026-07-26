from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f_map = Counter(s1)

        for i,ch in enumerate(s2):
            if ch in f_map:
                j = i
                state = True
                while j-i<len(s1):
                    if j<len(s2) and s2[j] in f_map and f_map[s2[j]]>0:
                        f_map[s2[j]]-=1
                    else:
                        state = False
                        f_map = Counter(s1)
                        break
                    j+=1
                if state:
                    return True

        return False
