# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        order = ""

        def helper(node):
            nonlocal order

            if not node:
                order += "N#"
                return
            
            order += f"{node.val}#"
            helper(node.left)
            helper(node.right)

        helper(root)
        return order
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split('#')[:-1]
        ind = 0

        print(data)

        def helper():
            nonlocal ind

            if data[ind]=='N':
                return None
            
            node = TreeNode(data[ind])

            ind+=1

            if node:
                node.left = helper()
            
            ind += 1

            if node:
                node.right = helper()

            return node
        
        return helper()

