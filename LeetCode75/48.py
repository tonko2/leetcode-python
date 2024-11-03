class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = [0] * (10 ** 5)
        for num in nums:
            count[num + 10 ** 4] += 1
        for i in range(10 ** 5, -1, -1):
            if count[i] > 0:
                k -= 1
                count[i] -= 1
            if k == 0:
                return i + 10 ** 4
            