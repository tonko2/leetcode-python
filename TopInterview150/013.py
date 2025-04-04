class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        products = 1
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                products *= num
        if zeros > 1:
            return [0] * len(nums)        
        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = products                
            else:
                if zeros:
                    nums[i] = 0                    
                else:
                    nums[i] = products // num
        return nums