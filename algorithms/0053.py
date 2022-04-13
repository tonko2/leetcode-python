from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       res = now = nums[0]
       N = len(nums)
       for i in range(1, N):
           now = max(nums[i], nums[i] + now)
           res = max(res, now)
       return res