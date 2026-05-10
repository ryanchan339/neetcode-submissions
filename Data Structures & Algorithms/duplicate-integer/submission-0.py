class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
            if freq[n] > 1:
                return True
        return False
        