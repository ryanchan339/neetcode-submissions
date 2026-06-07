# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            linked_list = lists[i]
            while linked_list != None:
                heap.append(linked_list.val)
                linked_list = linked_list.next

        heapq.heapify(heap)
        res = ListNode(0,None)
        curr = res
        while len(heap) != 0:
            val = heapq.heappop(heap)
            curr.next = ListNode(val, None)
            curr = curr.next
        res = res.next
        return res
        
