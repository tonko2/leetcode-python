class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        current_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if current_sum == (total_sum - nums[i] - current_sum):
                return i
            current_sum += nums[i]
        return -1