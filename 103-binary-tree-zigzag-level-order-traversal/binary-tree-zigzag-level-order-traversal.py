# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        isreverse=False
        d=deque()
        ans=[]
        if not root:
            return []
        d.append(root)
        while d:
            si=len(d)
            sub=[]
            for i in range(si):
                if not isreverse:
                    root=d.popleft()
                    sub.append(root.val)

                    if root.left!=None:
                        d.append(root.left)
                    if root.right!=None:
                        d.append(root.right)
                else:
                    root=d.pop()
                    sub.append(root.val)
                    if root.right:
                        d.appendleft(root.right)
                    if root.left:
                        d.appendleft(root.left)
                    
            isreverse=not isreverse
            ans.append(sub)
        return ans




        