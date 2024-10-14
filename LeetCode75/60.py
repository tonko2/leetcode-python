class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        ans = [float('inf')] * (N + 1)
        ans[0], ans[1] = 0, 0
        for i in range(2, N + 1):
            ans[i] = min(ans[i - 1] + cost[i - 1], ans[i - 2] + cost[i - 2])
        return ans[N]