import sys
import math
from collections import defaultdict, deque
from typing import List

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def comb(candidate, cnt):
            if cnt == N:
                if len(candidate):
                    ans.append(candidate)
                return
            num = int(digits[cnt])
            for c in alpha[num]:
                comb(candidate + c, cnt + 1)
        alpha = ["dummy", "dummy", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        N = len(digits)
        ans = []
        comb("", 0)
        return ans