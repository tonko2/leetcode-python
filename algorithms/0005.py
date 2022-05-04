import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        N = len(s)
        def f(left, right):
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        for i in range(N):
            res = max(res, f(i, i), f(i, i + 1))
        return ans