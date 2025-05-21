# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        current=head
        prev=None

        if head==None:
            return None
        
        while(current!=None):
            length+=1
            prev=current
            current=current.next
        print(length)
        k=k%length
        if k==0 or k==length:
            return head
        current=head
        print(prev.val)
        for i in range(length-k-1):
            current=current.next
        
        print(current.val)
        newhead=None
        if current.next:
            newhead=current.next
        current.next=None
        prev.next=head
        head=newhead
        return head





        