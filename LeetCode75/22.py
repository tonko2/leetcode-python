from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d = defaultdict(int)
        d2 = defaultdict(int)
        a = []
        b = []
        for i in range(len(word1)):
            d[word1[i]] += 1
            d2[word2[i]] += 1
        s = set()
        s2 = set()
        for key, value in d.items():
            a.append(value)
            s.add(key)
        for key, value in d2.items():
            b.append(value)        
            s2.add(key)
        if s != s2:
            return False
        a.sort()
        b.sort()
        return a == b