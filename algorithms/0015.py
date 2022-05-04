import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        doubles = set()
        nums.sort()
        ans = []
        d = defaultdict(int)
        for i, a in enumerate(nums):
            d[a] = max(d[a], i)
        for i in range(N):
            for j in range(i + 1, N):
                if (nums[i], nums[j]) in doubles:
                    continue
                doubles.add((nums[i], nums[j]))
                k = d[-(nums[i] + nums[j])]
                if k > j:
                    ans.append((nums[i], nums[j], nums[k]))
        return ans