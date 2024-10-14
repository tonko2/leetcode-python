from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        d = defaultdict(int)
        for num in nums:
            if d[num] == 0:
                nums[cnt] = num
                cnt += 1                
            d[num] += 1
        return cnt