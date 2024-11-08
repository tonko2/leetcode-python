class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        ans = 0
        for i in range(N):
            for j in range(i):
                if j == i - 1:
                    dp[i] = max(dp[i], dp[j])
                    dp[i] = max(dp[i], nums[i])
                else:
                    dp[i] = max(dp[i], dp[j] + nums[i])                
        for i in range(N):
            ans = max(ans, dp[i])            
        return ans