# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr != None:
            size += 1
            curr = curr.next
        res = None
        def reverseK(start, previous, index, first):
            nonlocal res
            if size - index < k:
                return start
            curr = start
            prev = previous
            for i in range(k):
                if i == k - 1:
                    if first:
                        res = curr
                    tmp = curr.next
                    curr.next = prev
                    start.next = tmp
                    if not first:
                        previous.next = curr
                else:
                    tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = tmp
            return start
        idx = 0
        curr = head
        res = head
        while curr and curr.next:
            if idx == 0:
                curr = reverseK(curr, None, idx, True)
            else:
                curr = reverseK(curr.next, curr, idx, False)
            idx += k
        return res