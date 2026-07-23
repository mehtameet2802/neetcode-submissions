# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key and not root.left and not root.right:
            return None

        def helper(node, key):
            if not node:
                return None


            if node.val != key:
                node.left = helper(node.left, key)
                node.right = helper(node.right, key)
                return node
            

            if node.right:

                new = node.right
                while new.left:
                    new = new.left
                
                node.val = new.val
                node.right = helper(node.right, node.val)
            
            elif node.left:
                new = node.left
                while new.right:
                    new = new.right
                
                node.val = new.val
                node.left = helper(node.left, node.val)
            else:
                node = None
            return node

        return helper(root, key)
