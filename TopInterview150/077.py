# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.stack = []
        return self._helper(root)
    
    def _helper(self, root):
        if not root:
            return 0
        
        prev = 10 * self.stack[-1] if len(self.stack) else 0
        self.stack.append(prev + root.val)

        if not root.left and not root.right:
            result = self.stack[-1]
            self.stack.pop()
            return result

        res = self._helper(root.left) + self._helper(root.right)
        self.stack.pop()
        return res