"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c_map = {}
        c_map[None] = None
        temp = head

        while temp:
            c_map[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        new_head = c_map[temp]
        while temp:
            c_map[temp].next = c_map[temp.next]
            c_map[temp].random = c_map[temp.random]
            temp = temp.next
        
        return new_head

        
