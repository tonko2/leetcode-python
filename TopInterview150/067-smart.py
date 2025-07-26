class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
            
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}
        
    def addNode(self, newNode):
        tmp = self.head.next
        self.head.next = newNode
        newNode.next = tmp
        newNode.prev = self.head
        tmp.prev = newNode
        
    def deleteNode(self, delNode):        
        prev = delNode.prev
        next = delNode.next
        prev.next = next
        next.prev = prev
    
    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]
            del self.m[key]
            self.deleteNode(node)
            self.addNode(node)
            self.m[key] = self.head.next
            return node.val
        return -1
    
    def put(self, key, value):
        if key in self.m:
            node = self.m[key]
            del self.m[key]
            self.deleteNode(node)
        
        if self.cap == len(self.m):
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        
        self.addNode(self.Node(key, value))
        self.m[key] = self.head.next