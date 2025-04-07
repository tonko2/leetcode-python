class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(left, right, x):            
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == x:
                    return mid
                if numbers[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        for i in range(len(numbers) - 1):
            idx = binary_search(i + 1, len(numbers) - 1, target - numbers[i])
            if idx != -1:
                return [i + 1, idx + 1]