class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            if tuple(points[i]) not in adj:
                adj[tuple(points[i])] = []
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if (x2, y2) not in adj:
                    adj[(x2,y2)] = []
                adj[(x1, y1)].append( (abs(x2 - x1) + abs(y2 -y1), (x2, y2)) )
                adj[(x2, y2)].append( (abs(x2 - x1) + abs(y2 -y1), (x1, y1)) )
        
        heap = [(0, tuple(points[0]))]
        res = 0
        a = tuple(points[0])
        visited = set()
        while len(visited) < len(points):
            curr = heapq.heappop(heap)
            if curr[1] in visited:
                continue
            res += curr[0]
            visited.add(curr[1])
            for e in adj[curr[1]]:
                heapq.heappush(heap, e)
                


        return res