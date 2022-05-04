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
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left = 0
        right = N - 1
        ans = 0
        while left < right:
            diff = right - left
            ans = max(ans, min(height[left], height[right]) * diff)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
