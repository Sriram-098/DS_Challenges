# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[-1e9]
        def maxsum(root):
            if root==None:
                return 0
            
            left=max(0,maxsum(root.left))
            right=max(0,maxsum(root.right))
            ans[0]=max(ans[0],left+right+root.val)
            return max(left,right)+root.val
        maxsum(root)
        return ans[0]
        