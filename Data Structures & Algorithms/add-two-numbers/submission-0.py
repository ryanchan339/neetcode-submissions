# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1 =
        [9,9,9,9,9,9,9]
        l2 =
        [9,9,9,9]
        
        89990001
        """
        carry = 0
        res = ListNode(0)
        curr = res

        while l1 and l2:
            currSum = l1.val + l2.val + carry
            carry = (currSum // 10) % 10
            curr.next = ListNode(currSum % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            currSum = l1.val + carry
            carry = (currSum // 10) % 10
            curr.next = ListNode(currSum % 10)
            curr = curr.next
            l1 = l1.next
        while l2:
            currSum = l2.val + carry
            carry = (currSum // 10) % 10
            curr.next = ListNode(currSum % 10)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return res.next

            