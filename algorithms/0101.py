from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isMirror(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not tree1 or not tree2:
            return tree2 == tree1
        if tree1.val != tree2.val:
            return False

        return self.isMirror(tree1.left, tree2.right) and self.isMirror(tree1.right, tree2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
