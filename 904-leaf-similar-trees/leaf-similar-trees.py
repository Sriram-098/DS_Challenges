# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def post(root,ls):
            if root==None:
                return None
            left=post(root.left,ls)
            right=post(root.right,ls)
            if not left and not right:
                ls.append(root.val)
            return root
        


        a=[]
        b=[]
        leftlist=post(root1,a)
        rightlist=post(root2,b)
        return a==b