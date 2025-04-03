from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        self.hash = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = 1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        del self.hash[val]
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.hash.keys()))


