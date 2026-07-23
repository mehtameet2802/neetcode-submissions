# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1001

        def helper(node):
            nonlocal ans

            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            side_max = max(left,right)

            ans = max(ans, node.val + side_max, left+right+node.val, node.val)

            return max(side_max + node.val, node.val)
        
        helper(root)
        return ans