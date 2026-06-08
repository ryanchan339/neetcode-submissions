class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = []
        for p in prerequisites:
            prereqs[p[0]].append(p[1])
        visited = set()
        visited2 = set()
        def dfs(p):
            if p in visited2:
                return True
            if p in visited:
                return False
            visited.add(p)
            for n in prereqs[p]:
                if dfs(n) == False:
                    return False
            visited.remove(p)
        
        for goal in prereqs.keys():
            for p in prereqs[goal]:
                visited.add(goal)
                if dfs(p) == False:
                    return False
                visited.clear()
                visited2.add(p)
            

        return True