# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        prev=dummy
        dummy.next=head

        curr=head
        while curr!=None:
            if curr.next and curr.val==curr.next.val:
                while curr.next and curr.val==curr.next.val:
                        curr=curr.next
                
                prev.next=curr.next
                curr=curr.next
            else:
                prev=prev.next
                curr=curr.next
        return dummy.next
        