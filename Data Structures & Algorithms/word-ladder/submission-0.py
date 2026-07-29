class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adj = {}
        words = set(wordList)
        for n in wordList:
            adj[n] = []
            for i in range(0, len(n)):
                for j in range(26):
                    if n[:i] + chr(ord('a') + j) + n[i + 1:] in words:
                        adj[n].append(n[:i] + chr(ord('a') + j) + n[i + 1:])


        adj[beginWord] = []
        for i in range(0, len(beginWord)):
            for j in range(26):
                if beginWord[:i] + chr(ord('a') + j) + beginWord[i + 1:] in words:
                    adj[beginWord].append(beginWord[:i] + chr(ord('a') + j) + beginWord[i + 1:])
           
        res = 1
        queue = deque()
        queue.append(beginWord)
        visited = set()
        parent = {}
        visited.add(beginWord)
        while queue:
            res += 1
            break1 = False
            for i in range(len(queue)):
                curr = queue.popleft()
                
                neighbors = adj.get(curr, [])
                for n in neighbors:
                    if n not in visited:
                        parent[n] = curr
                        visited.add(n)
                        queue.append(n)
                    if n == endWord:
                        parent[endWord] = curr
                        queue.clear()
                        break1 = True
                        break
                if break1:
                    break
        if endWord not in parent:
            return 0   
        """
        curr = endWord

        while curr != beginWord:
            res.append(curr)
            curr = parent[curr]
        res.append(beginWord)
        """
        return res