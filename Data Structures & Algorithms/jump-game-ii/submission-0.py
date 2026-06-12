class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float("inf")] * len(nums)

        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            minimum = float("inf")
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                minimum = min(minimum, 1 + dp[j])
            dp[i] = minimum


        return dp[0]