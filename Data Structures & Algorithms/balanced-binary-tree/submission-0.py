# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return 0, True
            
            l, s1 = helper(node.left)
            r, s2 = helper(node.right)

            if not s1 or not s2:
                return 0, False
            
            diff = abs(l-r)

            if diff<=1:
                return max(l,r)+1, True
            
            return max(l,r)+1, False
        
        _, ans = helper(root)
        return ans