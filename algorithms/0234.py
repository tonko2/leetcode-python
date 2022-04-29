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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversedList = None

        while fast is not None and fast.next is not None:
            tmp = slow
            slow = slow.next
            fast = fast.next.next

            tmp.next = reversedList
            reversedList = tmp

        if fast is not None:
            slow = slow.next

        while reversedList is not None and reversedList.val == slow.val:
            reversedList = reversedList.next
            slow = slow.next

        return reversedList is None
