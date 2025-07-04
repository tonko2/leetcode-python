# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        leftHead = left
        right = ListNode()
        rightHead = right
        pointer = head
        while pointer:
            if pointer.val < x:
                left.next = ListNode(pointer.val, None)
                left = left.next
            pointer = pointer.next
        pointer = head
        while pointer:
            if pointer.val >= x:
                right.next = ListNode(pointer.val, None)
                right = right.next
            pointer = pointer.next
        left.next = rightHead.next
        return leftHead.next