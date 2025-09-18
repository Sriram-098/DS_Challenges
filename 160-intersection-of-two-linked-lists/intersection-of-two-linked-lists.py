# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        def findlength(root):
            length=0
            while root:
                length+=1
                root=root.next
            return length
        
        head1Len=findlength(head1)
        head2Len=findlength(head2)

        diff=abs(head1Len-head2Len)
        if head1Len>head2Len:
            for _ in range(diff):
                head1=head1.next
        else:
            for _ in range(diff):
                head2=head2.next

        while head1 and head2:
            if head1==head2:
                return head1
            head1=head1.next
            head2=head2.next
        return None
    
        