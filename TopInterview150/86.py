# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        q = []
        def traverse(tree):
            if tree == None:
                return
            heapq.heappush(q, tree.val)
            traverse(tree.left)
            traverse(tree.right)
        traverse(root)
        ans = float('inf')
        prev = heapq.heappop(q)   
        while q:
            curr = heapq.heappop(q)
            ans = min(ans, abs(prev - curr))
            prev = curr
        return ans