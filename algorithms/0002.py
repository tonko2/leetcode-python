from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = l1.val + l2.val
        digit, carry = result % 10, result // 10
        answer = ListNode(digit)
        if any((l1.next, l2.next, carry)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += carry
            answer.next = self.addTwoNumbers(l1, l2)
        return answer