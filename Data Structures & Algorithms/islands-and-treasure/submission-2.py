class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        queue.append(None)
        distance = 0
        while queue:
            node = queue.popleft()

            if node == None:
                if queue:
                    distance += 1
                    queue.append(None)
                continue
            dirs = [(0,1), (1,0), (-1,0), (0,-1)]
            for i in range(4):
                
                nr, nc = node[0] + dirs[i][0], node[1] + dirs[i][1]
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 2147483647 and (nr,nc) not in visited:
                    queue.append((nr,nc))
                    visited.add((nr,nc))
                    grid[nr][nc] = distance + 1
        return
        