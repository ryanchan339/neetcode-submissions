class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        for i in range(1, len(s)):
            if s[i] == 0:
                if s[i - 1] != 1 and s[i - 1] != 2:
                    return 0
        """
        3127458
        10 20

        2234

        22054

        2 2 1 3
        22 1 3
        22 13
        2 2 13
        2 21 2
        """
        dp = {}
        def dfs(i):
            res = 0
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]
            if i + 1 < len(s) and '10' <= s[i:i+2] <= '26':
                res = dfs(i + 1)
                res += dfs(i + 2)
            else:
                res = dfs(i + 1)
            dp[i] = res
            return res
            
        return dfs(0)

        