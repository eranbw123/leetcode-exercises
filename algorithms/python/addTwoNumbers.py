# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = numbers = ListNode(None)
        while l1 or l2 or (carry == 1):
            n1=0;n2=0;
            if l1: n1 = l1.val
            if l2:  n2 = l2.val
            if (n1+n2+carry) >= 10:
                numbers.val = (n1 + n2 + carry) % 10
                carry = 1
            else:
                numbers.val = n1 + n2 + carry
                carry = 0
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            numbers.next = ListNode(None)
            prev = numbers
            numbers = numbers.next
        prev.next = None
        return head