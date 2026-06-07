class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cset, pdiag, ndiag = set(), set(), set()
        res = []
        board = [["."] * n for i in range(n)]
        def dfs(num, r):
            if num == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            for c in range(n):
                if (c not in cset and r + c not in pdiag and r - c not in ndiag):
                    cset.add(c)
                    pdiag.add(r+c)
                    ndiag.add(r-c)
                    board[r][c] = "Q"
                    dfs(num + 1, r + 1)
                    board[r][c] = "."
                    cset.remove(c)
                    pdiag.remove(r+c)
                    ndiag.remove(r-c)
        dfs(0, 0)
        return res