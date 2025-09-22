# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    order = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:        
        self.inorder_traversal(root)
        return self.order[k - 1]
    
    def inorder_traversal(self, node):
        if not node:
            return
        self.inorder_traversal(node.left)
        self.order.append(node.val)
        self.inorder_traversal(node.right)