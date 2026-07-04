class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = {}
        ans = []
        for word in strs:
            key = "".join(sorted(word))
            if key in s_map:
                s_map[key].append(word)
            else:
                s_map[key] = [word]
        
        for _, val in s_map.items():
            ans.append(val)

        return ans