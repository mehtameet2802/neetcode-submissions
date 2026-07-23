"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        clones = {}

        def helper(node):
            if not node:
                return None
            
            if node not in clones:
                clone = Node(node.val)
                clones[node] = clone
            else:
                return clones[node]

            for nei in node.neighbors:
                clone.neighbors.append(helper(nei))
            
            return clone
        
        return helper(node)
            