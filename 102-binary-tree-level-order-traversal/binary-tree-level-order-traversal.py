# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        ans=[]
        q.append(root)
        if not root:
            return []
        while q:
            sub=[]
            si=len(q)
            for i in range(si):
                root=q.popleft()
                sub.append(root.val)

                if root.left !=None:
                    q.append(root.left)

                if root.right!=None:
                    q.append(root.right)
            print(sub)

            ans.append(sub)

        return ans

            

            
        