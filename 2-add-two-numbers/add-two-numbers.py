# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry=0
        ans=ListNode(0)
        dummy=ans
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            x=val1+val2+carry

            carry=x//10
            rem=x%10

            ans.next=ListNode(rem)
            ans=ans.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next

        