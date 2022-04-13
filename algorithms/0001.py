from collections import defaultdict
from typing import List

def twoSum(nums, target):
    d = defaultdict(list)
    N = len(nums)
    for i in range(N):
        d[nums[i]].append(i)
    for i in range(N):
        l = d[target - nums[i]]
        if len(l):
            if nums[i] == target - nums[i]:
                if len(l) > 1:
                    return (i, l[1])
                else:
                    continue
            else:
                return (i, l[-1])

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec not in store:
                store[nums[i]]=i
            else:
                return [store[sec],i]