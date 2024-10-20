import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        cnt = bisect.bisect(nums, target)
        if cnt == 0:
            return 0
        elif nums[cnt - 1] == target:
            return cnt - 1
        elif nums[cnt - 1] < target:
            return cnt
        else:
            return cnt - 1