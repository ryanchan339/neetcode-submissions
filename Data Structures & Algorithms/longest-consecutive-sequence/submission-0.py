class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        numSet = set()
        for num in nums:
            numSet.add(num)
        maxLength = 1
        for num in numSet:
            length = 1
            if num - 1 not in numSet:
                while (num + 1 in numSet):
                    length += 1
                    num = num + 1
            if length > maxLength:
                maxLength = length
        return maxLength
