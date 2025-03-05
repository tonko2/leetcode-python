class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])
        ans = 0
        prev_x = -float('inf')        
        for sorted_point in sorted_points:
            x1, x2 = sorted_point
            if not x1 <= prev_x <= x2:
                ans += 1
                prev_x = x2
        return ans