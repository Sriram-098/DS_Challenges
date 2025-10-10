# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        prev=ListNode(0)
        prev.next=head
        dummy=prev
        for i in range(left-1):
            prev=prev.next
        curr=prev.next
        for _ in range(right-left):
            nextnode=curr.next
            curr.next=nextnode.next
            nextnode.next=prev.next
            prev.next=nextnode
        return dummy.next


        