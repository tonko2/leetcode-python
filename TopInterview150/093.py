from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        adj = [[] for _ in range(numCourses)]
        courses = [0] * numCourses
        ans = []
        
        for c, p in prerequisites:            
            adj[p].append(c)
            courses[c] += 1
            
        q = deque()
        for i in range(numCourses):
            if courses[i] == 0:
                q.append(i)
        
        while q:
            c = q.popleft()
            ans.append(c)
                        
            for next in adj[c]:
                courses[next] -= 1
                if courses[next] == 0:
                    q.append(next)
        
        return len(ans) == numCourses
    
s = Solution()
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(s.canFinish(numCourses, prerequisites))