class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = len(nums) - nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i + 1, len(nums)):
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
        return cnt