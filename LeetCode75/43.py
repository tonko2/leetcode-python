from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [False] * N        
        q = deque()
        q.append(0)
        count = 0
        while q:
            room = q.pop()
            if visited[room]:
                continue
            visited[room] = True
            count += 1
            for nextRoom in rooms[room]:
                q.append(nextRoom)
        return count == N
            