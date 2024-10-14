from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = defaultdict(int)
        magazineDict = defaultdict(int)
        for c in ransomNote:
            ransomNoteDict[c] += 1
        for c in magazine:
            magazineDict[c] += 1
        for key, value in ransomNoteDict.items():
            if magazineDict[key] < value:
                return False
        return True