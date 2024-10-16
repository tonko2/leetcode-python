# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        head = ListNode()
        while list1 != None or list2 != None:
            if not list1:
                head.next = ListNode(list2.val)
                list2 = list2.next
            elif not list2:
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    head.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    head.next = ListNode(list2.val)
                    list2 = list2.next       
            if res == None:
                res = head.next
            head = head.next
        return res
        