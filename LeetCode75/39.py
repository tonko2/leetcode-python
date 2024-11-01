# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        height = dict()
        def dfs(tree, h):
            if not tree:
                return
            if h in height:
                pass
            else:
                height[h] = tree.val
            dfs(tree.right, h + 1)
            dfs(tree.left, h + 1)
        dfs(root, 0)
        return list(height.values())