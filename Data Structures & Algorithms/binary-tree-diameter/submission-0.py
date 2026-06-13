# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        dm=0
        def dfs(root):
            nonlocal dm
            if root==None:
                return 0
            lh,rh = dfs(root.left),dfs(root.right)
            
            dm = max(dm,lh+rh)
            return 1+max(lh,rh)

        dfs(root)
        return dm