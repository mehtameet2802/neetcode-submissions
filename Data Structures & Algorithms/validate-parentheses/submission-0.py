class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{','[','(']
        closing = ['}',']',')']

        for char in s:
            if not stack:
                stack.append(char)
            else:
                top = stack[-1]
                if char in opening and top not in closing:
                    stack.append(char)
                elif top not in opening and char in closing:
                    stack.append(char)
                elif top=='{' and char=='}':
                    stack.pop()
                elif top=='(' and char==')':
                    stack.pop()
                elif top=='[' and char==']':
                    stack.pop()
                else:
                    stack.append(char)
        
        if not stack:
            return True

        return False
