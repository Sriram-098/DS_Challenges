# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(root):
            if root==p or root==q or root==None:
                return root


            left=find(root.left)
            right=find(root.right)

            if left==None:
                return right
            if right==None:
                return left
            return root




        return find(root)


        