# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def findlength(node):
            length=0
            while node:
                length+=1
                node=node.next
            return length
        lenA=findlength(headA)
        lenB=findlength(headB)

        diff=abs(lenA-lenB)
        if lenA>lenB:
            for _ in range(diff):
                headA=headA.next
        else:
            for _ in range(diff):
                headB=headB.next
        
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None


        