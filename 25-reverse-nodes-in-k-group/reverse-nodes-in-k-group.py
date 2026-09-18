# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        leng=0
        node=head
        while node!=None:
            leng+=1
            node=node.next
        
        curr=head
        prev=ListNode(0)
        prev.next=curr
        dummy=prev
        while leng>=k:
            
            for _ in range(k-1):
                nextnode=curr.next
                curr.next=nextnode.next
                nextnode.next=prev.next
                prev.next=nextnode

            leng-=k
            prev=curr
            curr=curr.next
        return dummy.next

            

        