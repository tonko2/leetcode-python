from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(zip(*grid))
        return sum(rows[row] for row in map(tuple, grid))