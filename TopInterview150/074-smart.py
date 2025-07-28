# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.q = []
        
        def preorder(node):
            if not node:
                return
            self.q.push(node)
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        
        if self.q:
            self.q.pop()
            
        while self.q:
            root.left = None
            root.right = self.q.pop()
            root = root.right