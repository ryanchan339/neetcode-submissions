class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total / 2

        prev_sums = set()
        for n in nums[:len(nums) - 1]:
            for x in prev_sums.copy():
                prev_sums.add(x + n)
            prev_sums.add(n)
            if half in prev_sums:
                return True
        if len(nums) > 1 and nums[-1] == half:
            return True
        return False
