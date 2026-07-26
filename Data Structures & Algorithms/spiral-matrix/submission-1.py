class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        ans = []

        while left<right and top<bottom:

            j = left
            while top<bottom and j<right:
                ans.append(matrix[top][j])
                j+=1
            
            top+=1
            i=top
            while left<right and i<bottom:
                ans.append(matrix[i][right-1])
                i+=1
            
            right-=1
            j = right-1
            while top<bottom and j>=left:
                ans.append(matrix[bottom-1][j])
                j-=1
            
            bottom-=1
            i = bottom-1
            while left<right and i>=top:
                ans.append(matrix[i][left])
                i-=1

            left+=1
        
        return ans
            
