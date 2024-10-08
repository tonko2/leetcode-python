class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        for x in nums:
            if x == 0:
                zeros += 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt += 1
        for i in range(zeros):
            nums[len(nums) - zeros + i] = 0