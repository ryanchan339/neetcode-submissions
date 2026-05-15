class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r,c) in visited:
                return False
            visited.add((r,c))
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and board[nr][nc] == 'O':
                    dfs(nr, nc)
            board[r][c] = 'A'
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'A':
                    board[r][c] = 'O'

