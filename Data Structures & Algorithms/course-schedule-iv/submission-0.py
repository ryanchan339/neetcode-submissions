class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for dst, src in prerequisites:
            adj[src].append(dst)
        
        dp = {} #set of prereqs

        def dfs(node):
            if node in dp:
                return dp[node]
            res = set()
            for nei in adj[node]:
                res.update(dfs(nei)) 
                res.add(nei)
            dp[node] = res
            return dp[node]
        for i in range(numCourses):
            dfs(i)
        answer = []
        #print(dp)
        for prq, course in queries:
            if prq in dp[course]:
                answer.append(True)
            else:
                answer.append(False)
        return answer
            