class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        digits = digits[::-1]
        digits[0] += 1        
        for i in range(len(digits)):
            if i == len(digits) - 1 and digits[i] == 10:
                digits[i] = 0
                digits.append(1)
            else:
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i + 1] += 1
        return digits[::-1]