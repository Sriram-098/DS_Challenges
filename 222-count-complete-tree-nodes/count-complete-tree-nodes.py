# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q=deque()
        ans=[]
        count=0
        q.append(root)
        if not root:
            return 0
        while q:
            sub=[]
            si=len(q)
            for i in range(si):
                root=q.popleft()
                count+=1
                sub.append(root.val)

                if root.left !=None:
                    q.append(root.left)

                if root.right!=None:
                    q.append(root.right)
            

            ans.append(sub)

        return count
        