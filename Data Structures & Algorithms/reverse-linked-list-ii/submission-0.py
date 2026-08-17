# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before, after = None, None
        dummy = ListNode(-1, head)
        curr = dummy
        for i in range(left - 1):
            curr = curr.next
        before = curr
        for i in range(right - left + 2):
            curr = curr.next
        after = curr
        def reverse(start, count): # return ptr to start and end of reversed
            #start is ptr, count is how many we are reversing
            prev, curr = None, start
            for i in range(count): 
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return (prev, start)
        start, end = reverse(before.next, right - left + 1)
        before.next = start
        end.next = after
    
        return dummy.next