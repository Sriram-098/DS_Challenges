# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        curr=head
        dummy=ListNode(0)
        prev=dummy
        prev.next=head
        while curr:
            count+=1
            curr=curr.next
        curr=head
        while count>=k:
            curr=prev.next
            for i in range(k-1):
                nextnode=curr.next
                curr.next=nextnode.next
                nextnode.next=prev.next
                prev.next=nextnode

            prev=curr
            count-=k
        return dummy.next

            
            
        
        