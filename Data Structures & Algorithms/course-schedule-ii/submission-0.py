class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deps = {}
        for i in range(numCourses):
            deps[i] = []
        for a, b in prerequisites:
            deps[a].append(b)
        res = []
        resSet = set()
        visited2 = set()
        def dfs(n, visited):
            if n in visited2:
                return True
            if n in visited:
                return False
            visited.add(n)
            if len(deps[n]) == 0:
                if n not in resSet:
                    res.append(n)
                    resSet.add(n)
                visited.remove(n)
                visited2.add(n)
                return True
            for prereq in deps[n]:
                if dfs(prereq, visited) == False:
                    visited.remove(n)
                    return False

            visited.remove(n)
            if n not in resSet:
                res.append(n)
                resSet.add(n)
            visited2.add(n)
            return True
                

        for i in range(numCourses):
            visited = set()
            if i in visited2:
                continue
            if dfs(i, visited) == False:
                return []
        
        if len(res) != numCourses:
            return []    
        return res