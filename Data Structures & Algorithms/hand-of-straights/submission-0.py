class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = {}
        for h in hand:
            freq[h] = freq.get(h, 0) + 1
        heap = hand.copy() #minheap
        heapq.heapify(heap)
        res = []
        for i in range(len(hand) // groupSize):
            curr = []
            while freq[heap[0]] == 0:
                heapq.heappop(heap)
            start = heapq.heappop(heap)
            freq[start] -= 1
            curr.append(start)
            for k in range(1, groupSize):
                num = start + k
                if num in freq and freq[num] > 0:
                    curr.append(num)
                    freq[num] -= 1
                else:
                    return False
            res.append(curr)
        return True
        