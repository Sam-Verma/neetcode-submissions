# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root==None:
                return 0,True
            
            lh,leftbalance=dfs(root.left)
            rh,rightbalance=dfs(root.right)

            h=1+max(lh,rh)

            if (lh-rh)>1 or (rh-lh)>1:
                return h,False
            
            elif leftbalance and rightbalance:
                return h,True
            
            else:
                return h, False
        
        h,balance=dfs(root)
        return balance