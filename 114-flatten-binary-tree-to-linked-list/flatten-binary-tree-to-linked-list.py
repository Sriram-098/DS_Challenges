# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def f(root):
            if not root:
                return None

            left=f(root.left)
            right=f(root.right)
            if left:
                root.right=left
                tail=left
                while tail.right:
                    tail=tail.right
                tail.right=right
                
            else:
                root.right=right
            root.left=None
            return root





        f(root)
       
        