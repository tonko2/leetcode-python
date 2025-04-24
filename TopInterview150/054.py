class MinStack:

    def __init__(self):
        self.stack = []
        self.count = 0

    def push(self, val: int) -> None:
        topMin = val
        if self.count > 0:
            topMin = min(self.stack[-1][1], val)
        self.stack.append((val, topMin))
        self.count += 1

    def pop(self) -> None:
        self.stack.pop()
        self.count -= 1

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]