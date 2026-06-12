class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0
        l = 0
        for r in range(len(nums)):
            while (l < r and curSum < 0):
                curSum -= nums[l]
                l += 1
            curSum += nums[r]
            if curSum > maxSum:
                maxSum = curSum
        return maxSum