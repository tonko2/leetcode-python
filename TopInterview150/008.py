class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(index, buy):
            if index >= len(prices):
                return 0
            if (index, buy) in memo:
                return memo[(index, buy)]
            res = 0
            if buy:
                by = dfs(index + 1, not buy) - prices[index]
                bn = dfs(index + 1, buy)
                res = max(by, bn)
            else:
                sy = dfs(index + 1, not buy) + prices[index]
                sn = dfs(index + 1, buy)
                res = max(sy, sn)
            memo[(index, buy)] = res
            return res            
        return dfs(0, True)