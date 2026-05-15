class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #visited set to keep track of visited tiles
        #dfs function to count area 
        visited = set()
        def dfs(r, c):
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            res = 1
            for i in range(4):
                dirs = [(0,1), (1,0), (-1,0), (0,-1)]
                nr, nc = r + dirs[i][0], c + dirs[i][1]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                    res += dfs(nr,nc)
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, dfs(i,j))
        return res
            