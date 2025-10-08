# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum=[-1e9]

        def backtrack(root):
            if root==None:
                return 0


            left=max(0,backtrack(root.left))
            right=max(0,backtrack(root.right))
            maxsum[0]=max(maxsum[0],left+right+root.val)


            return max(left,right)+root.val

        backtrack(root)
        return maxsum[0]
        