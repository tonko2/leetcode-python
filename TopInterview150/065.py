from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        N = 1
        pointer = head
        while pointer.next:
            pointer = pointer.next
            N += 1
        pointer.next = head
        k %= N
        print(f'N = {N}')
        for i in range(N - k + 1):
            pointer = pointer.next
        dummy = pointer
        for i in range(N - 1):
            pointer = pointer.next
        pointer.next = None
        return dummy