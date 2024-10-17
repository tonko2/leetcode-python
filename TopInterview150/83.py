# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = defaultdict(int)
        cnt = defaultdict(int)
        res = []
        def traverse(tree: [TreeNode], depth = 1):
            if tree == None:
                return
            d[depth] += tree.val
            cnt[depth] += 1
            traverse(tree.left, depth + 1)
            traverse(tree.right, depth + 1)
        traverse(root)
        for key, value in d.items():
            res.append(value / cnt[key])
        return res
        
        