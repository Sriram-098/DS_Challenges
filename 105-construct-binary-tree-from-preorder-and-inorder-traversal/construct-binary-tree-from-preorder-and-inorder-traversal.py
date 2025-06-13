# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping={}
        for i in range(len(inorder)):
            mapping[inorder[i]]=i

        deq=deque(preorder)
        print(deq)

        def build(start,end):
            if deq:
                if start >end:
                    return None

                val=deq.popleft()
                root=TreeNode(val)
                mid=mapping[val]

                root.left=build(start,mid-1)
                root.right=build(mid+1,end)

                return root

        return build(0,len(preorder))


            
            

        