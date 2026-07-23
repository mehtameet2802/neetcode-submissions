# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = -1

        def helper(node):
            nonlocal cnt
            nonlocal ans

            if cnt>=k:
                return

            if node.left:
                helper(node.left)

            cnt+=1
            if cnt == k:
                ans = node.val
                return
            
            if node.right:
                helper(node.right)
        
        helper(root)
        return ans




        