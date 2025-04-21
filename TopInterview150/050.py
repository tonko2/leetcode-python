class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for s, e in intervals:            
            if end >= s and e <= end:
                continue
            elif end >= s:
                end = e
            else:
                ans.append([start, end])
                start = s
                end = e
        ans.append([start, end])
        return ans