class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []

        def dfs(r, c, reachable):
            if (r,c) in reachable:
                return
            reachable.add((r,c))
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            for i in range(4):
                nr = r + dirs[i][0]
                nc = c + dirs[i][1]
                if (nr >= 0 and nr < len(heights) and nc >= 0 and nc < len(heights[0]) and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)
        pac = set()
        atl = set()
        for r in range(len(heights)):
            dfs(r,0,pac)
        for c in range(len(heights[0])):
            dfs(0,c,pac)
        for r in range(len(heights)):
            dfs(r,len(heights[0]) - 1,atl)
        for c in range(len(heights[0])):
            dfs(len(heights) - 1,c,atl)
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res