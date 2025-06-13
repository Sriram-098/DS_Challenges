# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans=[1e9]
        prev=[None]

        def check(root):
            if not root:
                return 

            left=check(root.left)
            if  prev[0] !=None:
                ans[0]=min(ans[0],root.val-prev[0])
            prev[0]=root.val
            right=check(root.right)

        check(root)
        return ans[0]






   
        
        