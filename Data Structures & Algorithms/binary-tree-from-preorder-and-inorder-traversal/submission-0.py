# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        i_map = {}
        
        for i, num in enumerate(inorder):
            i_map[num] = i

        preInd = 0

        def helper(l, r):
            nonlocal preInd

            if l > r:
                return None
            
            val = preorder[preInd]
            node = TreeNode(val)
            preInd += 1

            node.left = helper(l, i_map[val]-1)
            node.right = helper(i_map[val]+1,r)

            return node
        
        return helper(0, len(inorder)-1)
