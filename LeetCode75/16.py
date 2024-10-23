class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        ones = 0
        isOnes = False
        for num in nums:
            if num == 1:
                isOnes = True
                ones += 1
            else:
                isOnes = False
                ones = 0
            ans = max(ans, ones)
        left, right, cnt = 0, 0, 0
        while k > 0 and cnt <= k and right < len(nums):
            if nums[right] == 0:                
                while cnt == k and left < right:
                    if nums[left] == 0:
                        cnt -= 1
                    left += 1
                cnt += 1
            right += 1
            ans = max(ans, right - left)
        return ans