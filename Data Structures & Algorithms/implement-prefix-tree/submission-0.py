class TrieNode:
    def __init__(self,val=None, isEnd=False):
        self.val = val
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.trie
        for ch in word:
            if ch in trie.children:
                trie = trie.children[ch]
            else:
                new_node = TrieNode(ch)
                trie.children[ch] = new_node
                trie = new_node
        
        trie.isEnd = True

    def search(self, word: str) -> bool:
        trie = self.trie

        for ch in word:
            if ch not in trie.children:
                return False
            
            trie = trie.children[ch]
        
        return trie.isEnd

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie

        for ch in prefix:
            if ch not in trie.children:
                return False
            
            trie = trie.children[ch]
        
        return True
        
        