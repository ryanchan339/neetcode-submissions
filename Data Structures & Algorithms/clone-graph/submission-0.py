"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        newNode = Node(node.val)
        visited = set()
        mapping = {}
        def dfs(currNode, ogNode):
            if ogNode not in visited:
                visited.add(ogNode)
                mapping[ogNode] = currNode
                for n in ogNode.neighbors:
                    nextNode = None
                    if n in mapping:
                        nextNode = mapping[n]
                    else:
                        nextNode = Node(n.val)
                    currNode.neighbors.append(nextNode)
                    dfs(nextNode,n)
        dfs(newNode, node)

        return newNode