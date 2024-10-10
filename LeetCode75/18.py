class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        height = 0
        for h in gain:
            height += h
            ans = max(ans, height)
        return ans