class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack:
                stack.append(ast)
            else:
                if ast>0:
                    stack.append(ast)
                elif ast<0:
                    neg_ext = True
                    while stack and stack[-1]>0:
                        if abs(ast) == stack[-1]:
                            neg_ext = False
                            stack.pop()
                            break
                        elif abs(ast) < stack[-1]:
                            neg_ext = False
                            break
                        else:
                            stack.pop()
                    if neg_ext:
                        stack.append(ast)

        return stack