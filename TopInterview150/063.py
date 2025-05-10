from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next        
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        dummy = ListNode()
        dummy.next = head
        N = 0
        pointer = head
        while pointer:
            pointer = pointer.next
            N += 1
        pointer = dummy
        for i in range(N - n):
            pointer = pointer.next
        if pointer.next == None:
            pointer = None
        else:
            pointer.next = pointer.next.next
        return dummy.next