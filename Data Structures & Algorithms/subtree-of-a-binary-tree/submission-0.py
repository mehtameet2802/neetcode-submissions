# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False
            
            left = check(node1.left, node2.left)
            right = check(node1.right, node2.right)

            if not left or not right:
                return False
            
            if node1.val == node2.val:
                return True
            
            return False

        
        def helper(node):
            if not node:
                return False

            ans = False
            if node.val == subRoot.val:
                ans = check(node, subRoot)

            if ans:
                return True

            left = helper(node.left)
            right = helper(node.right)

            return left or right
        
        return helper(root)
        
        