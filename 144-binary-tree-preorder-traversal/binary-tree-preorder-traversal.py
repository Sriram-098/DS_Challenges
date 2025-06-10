# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        if not root:
            return []
        st.append(root)
        ans=[]
        while st:
            root =st.pop()
            ans.append(root.val)
            if root.right!=None:
                st.append(root.right)
            if root.left!=None:
                st.append(root.left)

        return ans

    
        