# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return True
        if head.val == float('inf'):
            return False
        head.val = float('inf')
        return self.hasCycle(head.next)