# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st=head
        middle=self.middle(head)
        reverse=self.reverse(middle)

        while st!=None and  reverse!=None:
            if st.val !=reverse.val:
                return False

            st=st.next
            reverse=reverse.next

        return True


    def middle(self,head):
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next

        return slow

    def reverse(self,head):
        prev=None
        current=head
        while(current!=None):
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode

        return prev

        