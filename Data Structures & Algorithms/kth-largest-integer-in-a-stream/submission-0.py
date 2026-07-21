class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxheap = []
        self.minheap = []
        self.capacity = k
        for n in nums:
            if len(self.minheap) == k:
                if n > self.minheap[0]:
                    heapq.heappush_max(self.maxheap, heapq.heappop(self.minheap))
                    heapq.heappush(self.minheap, n)
                else:
                    heapq.heappush_max(self.maxheap, n)
            else:
                heapq.heappush(self.minheap, n)
        

    def add(self, val: int) -> int:
        if len(self.minheap) == self.capacity:
            if val > self.minheap[0]:
                heapq.heappush_max(self.maxheap, heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, val)
                return self.minheap[0]
            else:
                heapq.heappush_max(self.maxheap, val)
                return self.minheap[0]
        else:
            heapq.heappush(self.minheap, val)
            return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)