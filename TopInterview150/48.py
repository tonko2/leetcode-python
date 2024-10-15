class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        prev = -1
        cnt = 0
        for i, num in enumerate(nums):
            if cnt == 0:
                prev = num
                cnt = 1
                continue
            if num - cnt == prev:
                cnt += 1
                continue
            if cnt == 1:
                ans.append(str(prev))                                
            else:
                ans.append("{}->{}".format(prev, nums[i - 1]))
            cnt = 1
            prev = num
        if cnt == 1:
            ans.append(str(prev))
        if cnt > 1:
            ans.append("{}->{}".format(prev, nums[-1]))
        return ans
