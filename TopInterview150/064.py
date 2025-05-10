from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1000, None)
        dummy.next = head
        pointer = dummy
        prevPointer = dummy
        prevValue = -2000
        while pointer:
            if pointer.next and pointer.val == pointer.next.val:            
                while pointer.next and pointer.val == pointer.next.val:
                    pointer = pointer.next
                prevPointer.next = pointer.next
            else:
                prevValue = pointer.val
                prevPointer = pointer
                
            pointer = pointer.next
                
        return dummy.next