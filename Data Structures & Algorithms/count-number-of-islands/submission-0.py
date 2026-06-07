class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        def bfs(x, y):
            nonlocal count
            if (x,y) not in visited and grid[x][y] == '1':
                count += 1
            else:
                return
            queue = deque()
            queue.append((x,y))
            visited.add((x,y))
            while queue:
                tile = queue.popleft()
                dirs = [(-1,0), (1,0), (0,-1), (0,1)]
                for dx, dy in dirs:
                    nx = dx + tile[0]
                    ny = dy + tile[1]
                    if ((nx, ny) not in visited and nx >= 0 and nx < len(grid) 
                    and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == '1'):
                        visited.add((nx,ny))
                        queue.append((nx,ny))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                bfs(i,j)
        return count
