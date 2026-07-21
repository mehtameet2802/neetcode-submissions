class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        c_map = {
            "+": lambda a,b: a + b,
            "*": lambda a,b: a * b,
            "-": lambda a,b: a - b,
            "/": lambda a,b: int(a / b)
        }

        for ele in tokens:
            if ele not in c_map:
                stack.append(int(ele))
            else:
                ele1 = stack.pop()
                ele2 = stack.pop()
                new_ele = c_map[ele](ele2,ele1)
                stack.append(new_ele)
        
        return stack[-1]

