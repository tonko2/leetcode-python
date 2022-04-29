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
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        N = len(prices)
        ans = 0
        for i in range(N):
            minimum = min(minimum, prices[i])
            ans = max(ans, prices[i] - minimum)
        return ans
