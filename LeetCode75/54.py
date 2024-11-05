import bisect
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        ans = []
        for spell in spells:
            ans.append(N - bisect.bisect_left(potions, math.ceil(success / spell)))
        return ans
        