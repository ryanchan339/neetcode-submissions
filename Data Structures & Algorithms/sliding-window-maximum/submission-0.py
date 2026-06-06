class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            lastSeen = {}
            heap = []
            res = []
            hset = set()

            for i in range(len(nums)):
                if i < k:
                    if nums[i] not in hset:
                        heapq.heappush_max(heap, nums[i])
                    hset.add(nums[i])
                    lastSeen[nums[i]] = i
                    if i + 1 == k:
                        res.append(heap[0])
                else:
                    while len(heap) and lastSeen[heap[0]] <= i - k:
                        hset.remove(heap[0])
                        heapq.heappop_max(heap)
                    if nums[i] not in hset:
                        heapq.heappush_max(heap, nums[i])
                    hset.add(nums[i])
                    lastSeen[nums[i]] = i
                    res.append(heap[0])
            return res
                
