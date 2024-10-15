class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsWithIndex = []
        for i, num in enumerate(nums):
            numsWithIndex.append((num, i))
        N = len(nums)
        def binary_search(x):
            left, right = 0, N - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numsWithIndex[mid][0] == x:
                    return numsWithIndex[mid][1]
                elif numsWithIndex[mid][0] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
    
        numsWithIndex.sort()
        for index, (num, i) in enumerate(numsWithIndex):
            targetValue = target - num            
            if targetValue == num:
                if index + 1 < N:
                    return [i, numsWithIndex[index + 1][1]]
                continue
            targetIndex = binary_search(targetValue)
            print(f'targetValue = {targetValue}')
            print(f'targeIndex = {targetIndex}')
            if targetIndex != -1:
                return (i, targetIndex)
        return [-1, -1]