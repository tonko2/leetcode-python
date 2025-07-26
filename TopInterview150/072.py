# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0

        def traverse(arr):
            if self.idx == len(preorder) or not arr:
                return None
            
            val = preorder[self.idx]
            valIndex = arr.index(val)
            self.idx += 1 
            
            left = arr[:valIndex]
            right = arr[valIndex + 1:]

            return TreeNode(val, traverse(left), traverse(right))
        
        return traverse(inorder)