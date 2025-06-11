# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def backtrack(root,sub):
            if root==None:
                return None
            
            sub.append(str(root.val))
            left=backtrack(root.left,sub)
            right=backtrack(root.right,sub)
            if left ==None and right==None:
                ans.append(sub[:])
            sub.pop()
            return root

        




        backtrack(root,[])
        print(ans)
        return ["->".join(i) for i in ans]