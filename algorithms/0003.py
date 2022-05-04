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
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        right = 1
        ans = 0
        alpha = defaultdict(int)
        for i in range(N):
            alpha[s[i]] = 1
            right = max(right, i + 1)
            while right < N and alpha[s[right]] == 0:
                alpha[s[right]] = 1
                right += 1
            alpha[s[i]] = 0
            ans = max(ans, right - i)
        return ans

    def lengthOfLongestSubstring_ans(self, s: str) -> int:
        seen = {}
        left, right = 0, 0
        ans = 0
        while right < len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            ans = max(ans, right - left + 1)
            seen[s[right]] = right
            right += 1
        return ans

hoge = Solution()
print(hoge.lengthOfLongestSubstring('abcabcbb'))
print(hoge.lengthOfLongestSubstring('bbbbb'))
print(hoge.lengthOfLongestSubstring('pwwkew'))
