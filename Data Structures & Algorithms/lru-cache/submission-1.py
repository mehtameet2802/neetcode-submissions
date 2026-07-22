class ListNode:
    def __init__(self, key=None, value=None, pre=None, nxt=None):
        self.key = key
        self.val = value
        self.pre = pre
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.k = capacity
        self.size = 0
        self.n_map = {}
        self.head = ListNode()
        self.end = ListNode()

        self.head.nxt = self.end
        self.end.pre = self.head
    
    def remove(self, node):
        node.nxt.pre = node.pre
        node.pre.nxt = node.nxt

        node.pre = node.nxt = None
        self.size -= 1
    
    def append(self, node):

        node.pre = self.end.pre
        self.end.pre.nxt = node
        node.nxt = self.end
        self.end.pre = node

        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.n_map:
            return -1
        
        node = self.n_map[key]
        self.remove(node)
        self.append(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.n_map:
            node = self.n_map[key]
            node.val = value
            self.remove(node)
        else:
            node = ListNode(key, value)
        
        if self.size == self.k:
            lru = self.head.nxt
            self.remove(lru)
            del self.n_map[lru.key]

        self.append(node)
        self.n_map[node.key] = node
        
