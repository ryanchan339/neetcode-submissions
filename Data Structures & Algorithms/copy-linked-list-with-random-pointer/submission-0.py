"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
nodes = {}
4 : 44
0 1 2 3 4 5

00 11 22 33 44 55

0 1 2 3 4 5
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mappings = {}
        curr1 = head

        res = None
        curr2 = None
        prev = None
        while (curr1):
            if res == None:
                curr2 = Node(curr1.val)
                res = curr2
                mappings[curr1] = curr2
                curr1 = curr1.next
            else:
                curr2.next = Node(curr1.val)
                curr2 = curr2.next
                mappings[curr1] = curr2
                curr1 = curr1.next
                

        curr1 = head
        curr2 = res
        while (curr1):
            if curr1.random is not None:
                curr2.random = mappings[curr1.random]
            curr1 = curr1.next
            curr2 = curr2.next
        
        return res

        
            