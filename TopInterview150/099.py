class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isWord = True
        
    def search(self, word):
        def dfs(node: TrieNode, index):
            if index == len(word):
                return node.isWord
            
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                    
            if word[index] in node.children:
                return dfs(node.children[word[index]], index + 1)
            
            return False
        
        return dfs(self.root, 0)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad"); # return False
wordDictionary.search("bad"); # return True
wordDictionary.search(".ad"); # return True
wordDictionary.search("b.."); # return True