class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxP = 0
        for p in piles:
            maxP = max(maxP, p)
        l, r = 1, maxP
        mid = 0
        while l < r:
            mid = (r + l) // 2
            hours_taken = 0
            for p in piles:
                hours_taken += (p // mid) + ((p % mid) > 0)
            if hours_taken > h:
                l = mid + 1
            else:
                r = mid

        return l