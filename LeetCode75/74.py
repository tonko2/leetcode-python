from collections import defaultdict

class Solution:
    def binary_search(self, arr ,x):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d = defaultdict(list)
        for index, t in enumerate(temperatures):
            d[t].append(index)
        ans = []
        
        for index, t in enumerate(temperatures):
            warmer = float('inf')            
            for i in range(t + 1, 101):
                if len(d[i]) == 0:
                    continue
                pos = self.binary_search(d[i], index)
                if pos == len(d[i]):
                    continue
                else:                    
                    warmer = min(warmer, d[i][pos] - index)                    
            if warmer == float('inf'):
                warmer = 0
            ans.append(warmer)
        return ans