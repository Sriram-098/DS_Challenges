# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        third=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while True:
                    if slow==third:
                        break
                    slow=slow.next
                    third=third.next

                    

                return slow
        return None


        
        