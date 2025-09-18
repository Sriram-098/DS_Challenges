# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        a=head1
        b=head2
        while a!=b:
            a=a.next if a else head2
            b=b.next if b else head1
        return a
        
    
        