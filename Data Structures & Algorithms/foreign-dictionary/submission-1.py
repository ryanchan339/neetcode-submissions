class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = ""
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {}
        currVisit = set()
        def dfs(c):
            nonlocal res
            if c in visited:
                return visited[c]
            if c in currVisit:
                return False
            currVisit.add(c)
            for node in adj[c]:
                if dfs(node) == False:
                    visited[c] = False
                    return False
            res += c
            currVisit.remove(c)
            visited[c] = True
            return True
        for a in adj:
            if dfs(a) == False:
                return ""
        return res[::-1]
            
                

        