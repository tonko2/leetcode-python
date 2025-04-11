class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = float('inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while left < i and total - nums[left] >= target:
                total -= nums[left]
                left += 1
            if total >= target:
                ans = min(ans, i - left + 1)
        return ans if ans != float('inf') else 0