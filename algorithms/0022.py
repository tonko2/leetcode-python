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
    def generateParenthesis(self, n: int) -> List[str]:
        def judge(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                else:
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        def gen(s, n):
            if n == N:
                if judge(s):
                    ans.append(s)
                return

            gen(s + '(', n + 1)
            gen(s + ')', n + 1)

        N = 2 * n
        ans = []
        gen('', 0)
        return ans
    def generateParenthesis_ans(self, n: int) -> List[str]:

        def backtrack(ans, curr, openp, closep, maxp):
            if len(curr) == 2 * maxp:
                ans.append(curr)
            if openp < maxp:
                backtrack(ans, curr + '(', openp + 1, closep, maxp)
            if closep < openp:
                backtrack(ans, curr + ')', openp, closep + 1, maxp)

        ans = []
        backtrack(ans, '', 0, 0, n)
        return ans