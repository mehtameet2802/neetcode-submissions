# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        sum = 0
        
        def helper(node):
            nonlocal sum
            if not node:
                return
            
            helper(node.right)
            sum += node.val
            node.val = sum
            helper(node.left)
            return
        
        helper(root)
        return root