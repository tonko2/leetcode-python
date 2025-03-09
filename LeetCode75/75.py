from collections import deque

class StockSpanner:

    def __init__(self):
        self.deque = deque()

    def next(self, price: int) -> int:        
        prev = 0
        while self.deque and self.deque[-1][0] <= price:            
            prev += self.deque[-1][1]
            self.deque.pop()
        ans = prev + 1
        self.deque.append((price, ans))
        return ans