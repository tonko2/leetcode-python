class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        now = float('inf')
        ans = 0
        for price in prices:
            if now > price:
                now = price
            else:
                ans = max(ans, price - now)
        return ans