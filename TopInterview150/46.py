class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsWithIndex = []
        for i, num in enumerate(nums):
            numsWithIndex.append((num, i))
        numsWithIndex.sort()        
        N = len(nums)
        for i in range(N - 1):
            if numsWithIndex[i][0] != numsWithIndex[i + 1][0]:                
                continue
            if numsWithIndex[i + 1][1] - numsWithIndex[i][1] <= k:
                return True
        return False
            