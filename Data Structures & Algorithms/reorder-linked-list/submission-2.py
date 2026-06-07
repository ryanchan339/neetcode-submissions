# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        listform = []
        length = 0
        curr = head
        while curr:
            listform.append(curr)
            curr = curr.next
            length += 1
        l, r = 0, length - 1

        while l <= r - 3:
            listform[l].next = listform[r]
            l += 1
            listform[r].next = listform[l]
            r -= 1
        if l + 1 == r:
            listform[l].next = listform[r]
            listform[r].next = None
        if l + 2 ==r:
            listform[l].next = listform[r]
            l += 1
            listform[r].next = listform[l]
            listform[l].next = None
        
        return None
                
        

        