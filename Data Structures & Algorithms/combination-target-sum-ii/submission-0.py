class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        set1 = set()
        #dp = {}
        # 1 1 2 5 6 7 10
        candidates.sort()
        def dfs(i, curr, currSum):
            
            if currSum == target:
                if tuple(curr) not in set1:
                    res.append(curr.copy())
                set1.add(tuple(curr))
                return
            if currSum > target:
                return
            if i == len(candidates):
                return
            curr.append(candidates[i])
            currSum += candidates[i]
            dfs(i + 1, curr, currSum)
            curr.pop()
            i += 1
            while i < len(candidates) and i >= 1:
                if candidates[i] == candidates[i - 1]:
                    i += 1
                else:
                    break
            dfs(i, curr, currSum - candidates[i - 1])
            
        dfs(0, [], 0)


        return res
