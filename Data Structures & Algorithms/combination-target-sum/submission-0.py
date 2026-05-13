class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
        def dfs(index, currSum):
            if currSum > target:
                return
            if currSum == target:
                res.append(curr.copy())
                return
            for i in range(index, -1, -1):
                curr.append(candidates[i])
                dfs(i, currSum + candidates[i])
                curr.pop()
        
        dfs(len(candidates) - 1, 0)
        return res

