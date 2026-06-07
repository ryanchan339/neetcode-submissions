class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        def backtrack(i, tmp):
            if (i >= len(nums)):
                return
            if (i >= 0):
                tmp.append(nums[i])
                res.append(tmp.copy())
            for j in range(i + 1, len(nums)):
                backtrack(j, tmp) 
            if (i >= 0):
                tmp.remove(nums[i])
        res.append([])
        backtrack(-1, tmp)
        return res