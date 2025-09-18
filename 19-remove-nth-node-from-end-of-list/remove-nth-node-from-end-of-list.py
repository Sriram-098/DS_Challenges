# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=1
        node=head
        while node.next!=None:
            length+=1
            node=node.next
        
        if length==k:
            return head.next
        
        
            
        if k>length:
            return -1
        
        node=head
        for i in range(length-k-1):
            node=node.next
            
        node.next=node.next.next
        
        return head
        