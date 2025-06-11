# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque()
        if not root:
            return 0
        q.append((root,0))
        maxi=0
        while q:
            _,level_head_index=q[0]
            siz=len(q)
            for i in range(siz):
                root,ind=q.popleft()

                current_ind=ind-level_head_index

                if root.left:
                    q.append((root.left,2*current_ind))
                if root.right:
                    q.append((root.right,2*current_ind+1))

            maxi=max(maxi,(q[-1][1]-q[0][1]+1 if q else 1))
        return maxi

        