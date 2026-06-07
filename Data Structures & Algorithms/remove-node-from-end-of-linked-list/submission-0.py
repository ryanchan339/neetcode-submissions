# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        nptr = head
        i = 0
        while i < n:
            nptr = nptr.next
            i += 1
        curr = head
        if not nptr:
            return head.next
        while nptr.next:
            curr = curr.next
            nptr = nptr.next
        nextNode = curr.next.next
        curr.next = nextNode
        return head