import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(x):
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / x)
            return cnt <= h
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left