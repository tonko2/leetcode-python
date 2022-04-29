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
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cnt == 0:
                candidate = nums[i]

            if candidate == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return candidate