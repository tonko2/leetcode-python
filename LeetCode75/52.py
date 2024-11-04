import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftHeap = []
        rightHeap = []
        N = len(costs)
        left, right = 0, N - 1
        
        for i in range(min(N, candidates)):
            heapq.heappush(leftHeap, costs[i])
            left += 1
        
        for i in range(N - 1, -1, -1):
            if len(rightHeap) == candidates:
                break
            if left >= right:
                break
            heapq.heappush(rightHeap, costs[i])
            right -= 1
        ans = 0
        while k:          
            if not leftHeap:
                ans += heapq.heappop(rightHeap)
                if left <= right:
                    heapq.heappush(rightHeap, costs[right])
                    right -= 1
            elif not rightHeap:
                ans += heapq.heappop(leftHeap)
                if left <= right:
                    heapq.heappush(leftHeap, costs[left])
                    left += 1
            else:
                if leftHeap[0] < rightHeap[0]:
                    ans += heapq.heappop(leftHeap)
                    if left <= right:
                        heapq.heappush(leftHeap, costs[left])
                        left += 1
                elif leftHeap[0] > rightHeap[0]:
                    ans += heapq.heappop(rightHeap)
                    if left <= right:
                        heapq.heappush(rightHeap, costs[right])
                        right -= 1
                else:
                    if costs[left] < costs[right]:
                        ans += heapq.heappop(leftHeap)
                        if left <= right:                        
                          heapq.heappush(leftHeap, costs[left])
                          left += 1
                    else:
                        ans += heapq.heappop(rightHeap)
                        if left <= right:
                            heapq.heappush(rightHeap, costs[right])
                            right -= 1
            k -= 1            
        return ans