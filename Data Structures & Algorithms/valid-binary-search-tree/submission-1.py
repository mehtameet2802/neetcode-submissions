# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = float('inf')

        def helper(node,l,r):
            if not node:
                return True
            
            if not l < node.val < r:
                return False
            
            l = helper(node.left, l, node.val)
            r = helper(node.right, node.val, r)

            return l and r
        
        return helper(root, -INF, INF)
