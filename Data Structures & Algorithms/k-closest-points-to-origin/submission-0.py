class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        if not points:
            return []
        for x,y in points:
            dists.append((x * x + y * y, (x,y)))
        heapq.heapify(dists)
        res = []
        for _ in range(k):
            top = heapq.heappop(dists)
            res.append(list(top[1]))
        return res