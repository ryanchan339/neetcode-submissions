class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(r, c):
            if (r,c) in dp:
                return dp[(r,c)]
            if r == m - 1 and c == n - 1:
                dp[(r,c)] = 1
                return dp[(r,c)]
            if r > m - 1 or c > n - 1:
                return 0
            dp[(r,c)] = dfs(r + 1, c)
            dp[(r,c)] += dfs(r, c + 1)
            return dp[(r,c)]


        dfs(0,0)
        return dp[(0,0)]