# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        
        dummy=ListNode(0)
        prev=dummy
        dummy.next=head

        while count>=k:
            curr=prev.next
            for _ in range(k-1):
                nextnode=curr.next
                curr.next=nextnode.next
                nextnode.next=prev.next
                prev.next=nextnode
            
            count-=k
            prev=curr
        return dummy.next
        