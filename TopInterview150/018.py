class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        N = len(nums)
        ans = []
        for i in range(N - 1, -1, -1):
            d = num // nums[i]
            num -= nums[i] * d
            ans.append(romans[i] * d)
        return "".join(ans)