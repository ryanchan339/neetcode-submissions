class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        heap = ([(val, key) for key, val in hashmap.items()])
        heapq.heapify(heap)
        frequencies = heapq.nlargest(k, heap)
        res = []
        for n,c in frequencies:
            res.append(c)
        return res