# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        height = defaultdict(int)
        def dfs(root, h):
            if not root:
                return
            height[h] += root.val
            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
        dfs(root, 1)
        ans = 1
        sum = height[1]
        for key, value in height.items():            
            if sum < value:
                sum = value
                ans = key
        return ans