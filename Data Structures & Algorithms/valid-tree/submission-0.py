class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {}
        for i in range(n):
            adj[i] = []
        for e in edges:
            src, dest = e
            if src not in adj:
                adj[src] = []
            if dest not in adj:
                adj[dest] = []
            adj[src].append(dest)
            adj[dest].append(src)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nb in adj[node]:
                if nb == prev:
                    continue
                if dfs(nb, node) == False:
                    return False
            return True
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                if dfs(i, None) == False:
                    return False
        return True if components == 1 else False