# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        hash = {}
        def sumPath(tree: TreeNode, sum: int = 0):
            if tree == None:
                return
            if tree.left == None and tree.right == None:
                hash[sum + tree.val] = True
                return            
            sumPath(tree.left, sum + tree.val)
            sumPath(tree.right, sum + tree.val)        
        sumPath(root)
        return True if hash.get(targetSum) else False