import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.infiniteSet = []
        self.cnt = 1
        self.count = set()
        heapq.heapify(self.infiniteSet)

    def popSmallest(self) -> int:
        if len(self.infiniteSet) and self.infiniteSet[0] == self.cnt:
            self.cnt += 1
            self.count.remove(self.infiniteSet[0])
            return heapq.heappop(self.infiniteSet)
        elif len(self.infiniteSet) and self.infiniteSet[0] < self.cnt:
            self.count.remove(self.infiniteSet[0])
            return heapq.heappop(self.infiniteSet)
        else:
            self.cnt += 1
            return self.cnt - 1

    def addBack(self, num: int) -> None:
        if num in self.count:
            return
        heapq.heappush(self.infiniteSet, num)
        self.count.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)