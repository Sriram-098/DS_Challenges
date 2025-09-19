# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathsum=[-1e9]
        def rec(root):
            if root==None:
                return 0
            
            left=max(rec(root.left),0)
            right=max(rec(root.right),0)
            pathsum[0]=max(pathsum[0],right+left+root.val)
            
            
            return max(left,right)+root.val
            
            
        
        rec(root)
        return pathsum[0]
        