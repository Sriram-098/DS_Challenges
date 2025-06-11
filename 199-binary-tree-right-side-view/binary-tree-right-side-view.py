# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        q=deque()
        if not root:
            return []
        q.append(root)
        while q:
            si=len(q)
            for i in range(si):
                root=q.popleft()
                if i==si-1:
                    ans.append(root.val)

                if root.left!=None:
                    q.append(root.left)
                if root.right!=None:
                    q.append(root.right)
        return ans
        