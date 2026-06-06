class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        heap = []
        #(temp, index)
        for i in range(len(temperatures)):
            while len(heap) > 0 and heap[0][0] < temperatures[i]:
                temp, index = heapq.heappop(heap)
                res[index] = i - index
            heapq.heappush(heap, (temperatures[i],i))
        return res