# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(tree, maxVal):
            if not tree:
                return 0            
            cnt = 0
            if maxVal <= tree.val:
                cnt = 1
            return cnt + count(tree.left, max(maxVal, tree.val)) + count(tree.right, max(maxVal, tree.val))
        return count(root, root.val)