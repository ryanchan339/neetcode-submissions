class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        curr = []
        dp = {}

        def dfs(i):
            if i == len(nums):
                res.add(tuple(curr.copy()))
                return
            
            dfs(i + 1)
            curr.append(nums[i])
            dfs(i + 1)
            curr.remove(nums[i])
        
        dfs(0)

        return list(res)
