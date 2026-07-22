class Solution:
    def decodeString(self, s: str) -> str:
        
        r = 0
        stack = []
        

        while r < len(s):
            if s[r] == '[':
                stack.append(s[r])
                r+=1
            elif s[r].isdigit():
                num = ""
                while r<len(s) and s[r] != '[':
                    num += s[r]
                    r += 1
                stack.append(int(num))
                continue
            elif s[r] == ']':
                s2 = ""
                while stack[-1]!='[':
                    s2 = stack[-1] + s2
                    stack.pop()
                r+=1
                stack.pop()
                num = stack.pop()
                s2 = num*s2
                stack.append(s2)
            else:
                s1 = ""
                while r<len(s) and (s[r]!=']' and not s[r].isdigit()):
                    s1 += s[r]
                    r+=1
                stack.append(s1)
        
        ans = ""
        while stack:
            ans = stack.pop() + ans
        
        return ans

