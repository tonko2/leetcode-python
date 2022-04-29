import sys
import math
from collections import defaultdict, deque
from typing import Optional

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

    def reverseList_rec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        smallHead = self.reverseList_rec(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return smallHead