class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for n in adj[i]:
                dfs(n)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count