class TrieNode:
    def __init__(self, val=None, isEnd=False):
        self.val = val
        self.children = {}
        self.isEnd = isEnd

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.trie

        for ch in word:
            if ch in trie.children:
                trie = trie.children[ch]
                continue
            
            new_node = TrieNode(ch)
            trie.children[ch] = new_node
            trie = new_node
        
        trie.isEnd = True
            

    def search(self, word: str) -> bool:
        trie = self.trie

        def helper(t, w1):
            for i, ch in enumerate(w1):
                if ch == '.':
                    ans = False
                    for child in t.children.values():
                        ans = ans or helper(child, w1[i+1:])
                    return ans
                
                elif ch not in t.children:
                    return False
                else:
                    t = t.children[ch]
            
            return t.isEnd
        
        return helper(trie, word)
