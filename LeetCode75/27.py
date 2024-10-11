from collections import deque

class RecentCounter:
    d = deque()
    def __init__(self):
        self.d = deque()

    def ping(self, t: int) -> int:
        self.d.append(t)
        while self.d[-1] - self.d[0] > 3000:
            self.d.popleft()
        return len(self.d)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)