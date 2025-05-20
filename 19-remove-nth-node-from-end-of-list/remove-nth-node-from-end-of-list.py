# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current=head
        length=0
        while(current!=None):
            length+=1
            current=current.next
        current=head
        
        if length==n:
            return head.next
        for i in range(length-n-1):
            current=current.next
        if current.next:
            current.next=current.next.next

        return head
    

        