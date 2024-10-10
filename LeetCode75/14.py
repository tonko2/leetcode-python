class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:        
        sum = 0
        for i in range(k):
            sum += nums[i]
        ans = sum
        for i in range(len(nums) - k):
            sum = sum - nums[i] + nums[i + k]
            ans = max(ans, sum)                
        return ans / k