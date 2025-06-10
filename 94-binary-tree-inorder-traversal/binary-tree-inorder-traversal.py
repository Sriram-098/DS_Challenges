# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        st=[]
        if not root:
            return []
        
        while True:
            if root:
                st.append(root)
                root=root.left
                
                
            else:
                if not st:
                    break
                root=st.pop()
                ans.append(root.val)
                root=root.right
        return ans

        