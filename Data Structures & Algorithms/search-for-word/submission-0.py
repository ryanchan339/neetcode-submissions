class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visiting = set()
        if word == "":
            return True
        def dfs(i, r, c):
            if (r,c) in visiting:
                return False
            if board[r][c] != word[i]:
                return False
            visiting.add((r,c))
            if i == len(word) - 1:
                return True
            dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
            for j in range(4):
                nr = r + dirs[j][0]
                nc = c + dirs[j][1]
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                    continue
                if dfs(i + 1, nr, nc) == True:
                    visiting.remove((r,c))
                    return True
            visiting.remove((r,c))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j) == True:
                    return True
        return False