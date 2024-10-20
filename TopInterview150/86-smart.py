class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(r):
            res=[]
            if r.left:
                res+=inorder(r.left)
            res.append(r.val)
            if r.right:
                res+=inorder(r.right)
            return res
        arr=inorder(root)
        m=float('inf')
        for i in range(len(arr)-1):
            m=min(m,arr[i+1]-arr[i])
        return m