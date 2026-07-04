class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for opt in operations:
            if opt == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                num1 = num1+num2
                stack.append(num1)
            
            elif opt == "C":
                stack.pop()

            elif opt == "D":
                num1 = stack[-1]
                num1 = num1 * 2
                stack.append(num1)
            else:
                stack.append(int(opt))
        
        total = 0
        while stack:
            total += stack[-1]
            stack.pop()

        return total