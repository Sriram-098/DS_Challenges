# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
     
        curr=head
        initialnode=head
        length=1
        
        while curr.next!=None:
            length+=1
            curr=curr.next
        lastnode=curr
        k=k%length
        if k==0 or k==length:
            return head
        curr=head
        for _ in range(length-k-1):
            curr=curr.next
        startnode=None
        if curr.next:
            startnode=curr.next
            
        curr.next=None
        lastnode.next=initialnode
        return startnode
        


        