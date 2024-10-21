import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        zeros = 0
        p = 1
        for num in nums:
            if num == 0:
                zeros += 1
        if zeros > 1:
            return [0] * len(nums)        
        elif zeros == 1:
            for num in nums:
                if num != 0:
                    p *= num
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = p
                else:
                    nums[i] = 0
        else:
            p = math.prod(nums)
            for i in range(len(nums)):
                nums[i] = p // nums[i]
        return nums