# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev=[None]

        def check(root):
            if not root:
                return True

            left=check(root.left)
            if  prev[0] is not None and prev[0] >=root.val:
                return False
                
            prev[0]=root.val
            right=check(root.right)

            return left and right

        return check(root)
        
        