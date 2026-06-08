class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(x):
            if x in cache:
                return cache[x]
            if x <= 2:
                return x
            cache[x] = dfs(x-1) + dfs(x-2)
            return cache[x]
        return dfs(n)