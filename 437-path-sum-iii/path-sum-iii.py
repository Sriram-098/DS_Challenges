# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d={0:1}
        count=[0]
        s=0

        def backtrack(root,prefix_s,d):
            if not root:
                return None
            
            prefix_s+=root.val
            #print(d)
            count[0]+=d.get(prefix_s-targetSum,0)
            d[prefix_s]=d.get(prefix_s,0)+1
            
            left=backtrack(root.left,prefix_s,d)
            right=backtrack(root.right,prefix_s,d)

            if prefix_s in d:
                d[prefix_s]-=1
            else:
                del d[prefix_s]



            return root





        backtrack(root,s,d)
        return count[0]
        