class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float("inf")] * n
        adj = {}
        for s, d, p in flights:
            if s not in adj:
                adj[s] = []
            adj[s].append((d, p))
        dist[src] = 0
        queue = deque()
        queue.append(src)

        level = 0
        while queue and level < k + 1:
            level += 1
            curr_dist = dist.copy()
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr not in adj:
                    continue
                for d, p in adj[curr]:
                    if p + curr_dist[curr] < dist[d]:
                        dist[d] = p + curr_dist[curr]
                        queue.append(d)
        return dist[dst] if dist[dst] != float("inf") else -1
            