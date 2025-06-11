# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=[0]
        def find(root):
            if not root:
                return 0


            left=find(root.left)
            right=find(root.right)
            dia[0]=max(right+left,dia[0])


            return 1+max(left,right)



        find(root)
        return dia[0]
        