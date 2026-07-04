# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0,True
            
            lh,left=dfs(root.left)
            rh,right=dfs(root.right)
            
            balance = left and right and abs(lh-rh)<=1
            
            return 1+max(lh,rh),balance
        
        h,balance=dfs(root)
        return balance