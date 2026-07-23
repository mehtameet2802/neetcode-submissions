class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        c_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r', 's'],
            '8': ['t','u','v'],
            '9': ['w','x','y', 'z'],
        }

        ans = []
        res = []

        def helper(i):
            if i>=len(digits):
                ans.append("".join(res))
                return
            
            for ch in c_map[digits[i]]:
                res.append(ch)
                helper(i+1)
                res.pop()
            
        helper(0)
        return ans