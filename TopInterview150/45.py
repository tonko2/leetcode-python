class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {}
        while n not in nums:
            sum = 0
            nums[n] = 1
            while n:                
                sum += (n % 10) ** 2
                n //= 10
            if sum == 1:
                return True                
            n = sum            
        return False
        