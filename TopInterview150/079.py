# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order = []
        self.preorder_traversal(root)        
        
    def preorder_traversal(self, node):        
        if not node:
            return
        if node.left:
            self.preorder_traversal(node.left)
        self.order.append(node.val)
        if node.right:
            self.preorder_traversal(node.right)        
        return

    def next(self) -> int:
        return self.order.pop(0)

    def hasNext(self) -> bool:
        return True if len(self.order) else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()