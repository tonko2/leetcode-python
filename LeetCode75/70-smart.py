class TrieNode:
    def __init__(self):
        self.children = {}        
        self.suggestions = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)            
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        ans = []
        node = trie.root
        for c in searchWord:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            ans.append(node.suggestions)                         
            
        return ans