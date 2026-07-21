class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            one = heapq.heappop_max(stones)
            two = heapq.heappop_max(stones)
            if one != two:
                heapq.heappush_max(stones, one - two)
        if len(stones):
            return stones[0]
        return 0