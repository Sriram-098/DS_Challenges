# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[None]
        count=[0]
        

        
        def check(root):
     
            if not root:
                return None

            left=check(root.left)
            count[0]+=1
            if count[0]==k:
                ans[0]= root.val
                return
            
           
             
            right=check(root.right)
            

        check(root)
        return ans[0]
        
        