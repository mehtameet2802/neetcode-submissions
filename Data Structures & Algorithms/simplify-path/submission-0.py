class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        final_path = path.split('/')

        print(final_path)
        for file in final_path:
            if file == '.' or file == '':
                continue
            elif file == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(file)
        
        return "/" + "/".join(stack) 
        