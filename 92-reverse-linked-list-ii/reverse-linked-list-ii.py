# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        curr=head
        prev= ListNode(0)
        prev.next=curr
        dummy=prev
        if head.next==None:
            return head
        for i in range(left-1):
            curr=curr.next
            prev=prev.next
        print(prev.val)
        for i in range(right-left):
            nextnode =curr.next
            curr.next=nextnode.next
            nextnode.next=prev.next
            prev.next=nextnode

        return dummy.next

        

        
        