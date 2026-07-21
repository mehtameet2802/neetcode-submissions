# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        def helper(node):
            nonlocal ans

            if not node:
                return
            
            if not node.left and not node.right:
                ans.append(node.val)
                return
            
            ans.append(node.val)
            helper(node.left)
            helper(node.right)

            return
        
        helper(root)
        return ans