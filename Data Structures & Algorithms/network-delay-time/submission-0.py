class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        V = n
        adj = {}
        for a, b, c in times:
            if a not in adj:
                adj[a] = []
            adj[a].append((b,c))
        print(adj)

        # Min-heap (priority queue) storing pairs of (distance, node)
        heap = []

        dist = [float("inf")] * (V + 1)

        # Distance from source to itself is 0
        dist[k] = 0
        heapq.heappush(heap, (0, k))

        # Process the queue until all reachable vertices are finalized
        while heap:
            d, u = heapq.heappop(heap)

            # If this distance not the latest shortest one, skip it
            if d > dist[u]:
                continue

            # Explore all neighbors of the current vertex
            if u not in adj:
                continue
            for v, w in adj[u]:

                # If we found a shorter path to v through u, update it
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        # Return the final shortest distances from the source
        for i in range(1, len(dist)):
            if dist[i] == float("inf"):
                return -1
        print(dist)
        return max(dist[1:])