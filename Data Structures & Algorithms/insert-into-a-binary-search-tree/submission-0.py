# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def helper(node, val):
            if not node:
                return TreeNode(val)

            if node.val > val:
                node.left = helper(node.left, val)
            else:
                node.right = helper(node.right, val)
            
            return node
        
        helper(root, val)
        return root