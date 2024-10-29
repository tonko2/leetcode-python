# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        ans = 0
        for i in range(len(A) // 2):
            ans = max(ans, A[i] + A[len(A) - 1 - i])
        return ans