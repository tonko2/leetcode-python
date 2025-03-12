class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        
    def search(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd
    
    def startsWith(self, prefix: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
        return True
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        ans = []
        
        return ans