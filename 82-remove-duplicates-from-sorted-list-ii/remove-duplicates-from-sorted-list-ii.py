# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev=ListNode(0)
        curr=head
        prev.next=head
        dummy=prev
        while curr:
            if curr.next!=None and curr.val==curr.next.val:
                while curr.next and curr.val==curr.next.val:
                    curr.next=curr.next.next
                prev.next=curr.next
                curr=curr.next

                
            else:
                prev=curr
                curr=curr.next
        return dummy.next



        
        