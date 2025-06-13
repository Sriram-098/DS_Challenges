# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping={}
        for i in range(len(inorder)):
            mapping[inorder[i]]=i

        deq=deque(postorder)
        print(deq)

        def build(start,end):
            
            if start >end:
                return None

            val=deq.pop()
            root=TreeNode(val)
            mid=mapping[val]
            
            root.right=build(mid+1,end)
            root.left=build(start,mid-1)
            

            return root

        return build(0,len(postorder)-1)
        