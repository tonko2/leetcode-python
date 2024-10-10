from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for x in arr:
            d[x] += 1
        occurrences = defaultdict(int)
        for key, value in d.items():
            if occurrences[value]:
                return False
            occurrences[value] = key
        return True
        