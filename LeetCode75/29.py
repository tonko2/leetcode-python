# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:                            
            fast = fast.next.next            
            slow = slow.next
        deletedHead = head
        while True:
            if deletedHead.next == slow:
                deletedHead.next = deletedHead.next.next
                break
            deletedHead = deletedHead.next
        return head
        