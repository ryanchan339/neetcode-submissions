class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        queue.append(None)
        while queue:
            node = queue.popleft()
            if node == None:
                res += 1
                if queue:
                    queue.append(None)
                continue
            
            dirs = [(1,0), (0,1), (0,-1), (-1,0)]
            for i in range(4):
                #add bounds check
                if (node[0] + dirs[i][0] >= 0 and node[0] + dirs[i][0] < len(grid) and node[1] + dirs[i][1] >= 0 and node[1] + dirs[i][1] < len(grid[0]) and (node[0] + dirs[i][0], node[1] + dirs[i][1]) not in visited and grid[node[0] + dirs[i][0]][node[1] + dirs[i][1]] == 1):
                    grid[node[0] + dirs[i][0]][node[1] + dirs[i][1]] = 2
                    queue.append((node[0] + dirs[i][0], node[1] + dirs[i][1]))
                    visited.add((node[0] + dirs[i][0], node[1] + dirs[i][1]))

        #go through to check if any fresh orange
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res - 1