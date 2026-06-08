class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = cost.copy()
        for i in range(len(cost) - 3, -1, -1):
            dp[i] = min(dp[i] + dp[i + 1], dp[i] + dp[i + 2])
        return min(dp[0], dp[1])