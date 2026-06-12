class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = {}
        dp[len(nums) - 1] = True
        def dfs(i):
            if i in dp:
                return dp[i]
            if nums[i] == 0 and i != len(nums) - 1:
                dp[i] = False
                return False

            for j in range(min(len(nums), i + nums[i] + 1) - 1, i, -1):
                if dfs(j):
                    dp[i] = True
                    return True
            dp[i] = False    
            return False
        dfs(0)
        return dp[0]
        