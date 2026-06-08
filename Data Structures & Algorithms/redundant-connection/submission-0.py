class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for s, d in edges:
            if s not in adj:
                adj[s] = []
            if d not in adj:
                adj[d] = []
            adj[s].append(d)
            adj[d].append(s)


        visiting = set()
        cycleEdges = set()
        def dfs(prev, node):
            if node in visiting:
                return node
            visiting.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                cycleNode = dfs(node, nei)
                if cycleNode == -1:
                    return -1
                if cycleNode:
                    if nei < node:
                        cycleEdges.add((nei, node))
                    else:
                        cycleEdges.add((node, nei))
                    if node == cycleNode:
                        return -1
                    return cycleNode
            return 0
        dfs(None, 1)
        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            if tuple(edge) in cycleEdges:
                return edge
        
            
            

