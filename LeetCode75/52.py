import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = []
        right_heap = []
        n = len(costs)
        left = candidates - 1
        right = n - 1
        ans = 0
        for i in range(candidates):
            heapq.heappush(left_heap, costs[i])
        for i in range(candidates):
            if n - 1 - i <= left:
                break
            right = n - 1 - i
            heapq.heappush(right_heap, costs[n - 1 - i])        
        while k:            
            if len(left_heap) == 0 and len(right_heap) == 0:
                break
            if len(left_heap) == 0:
                ans += sum(heapq.nsmallest(k, right_heap))
                break
            if len(right_heap) == 0:
                ans += sum(heapq.nsmallest(k, left_heap))
                break
            if left_heap[0] <= right_heap[0]:
                ans += heapq.heappop(left_heap)
                if left + 1 < right:
                    left += 1
                    heapq.heappush(left_heap, costs[left])
            else:
                ans += heapq.heappop(right_heap)
                if left < right - 1:
                    right -= 1
                    heapq.heappush(right_heap, costs[right])
            k -= 1
        return ans
        
        