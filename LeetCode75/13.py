from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        ans = 0
        for num in nums:
            if d[num] == 0:
                continue
            d[num] -= 1
            if d[k - num] > 0:
                d[k - num] -= 1
                ans += 1
        return ans