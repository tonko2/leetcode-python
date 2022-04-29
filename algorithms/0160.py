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
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        S = set()
        while headA != None:
            S.add(headA)
            headA = headA.next
        while headB != None:
            if headB in S:
                return headB
            headB = headB.next

        return None
    def getIntersectionNode_ans(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hA = headA
        hB = headB
        while hA != hB:
            hA = headB if not hA else hA.next
            hB = headA if not hB else hB.next
        return hA
