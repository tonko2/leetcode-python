# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def check(tree, total):            
            if not tree:
                return 0
            res = 0
            if (total + tree.val) == targetSum:
                res = 1
            return res + check(tree.left, total + tree.val) + check(tree.right, total + tree.val)
        def dfs(tree):            
            if not tree:
                return 0            
            cnt = check(tree, 0)                
            return cnt + dfs(tree.left) + dfs(tree.right)
        return dfs(root)