class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        numSet = set()
        curr = []
        """
        numset 2 1 3

        curr 2 1 3 
        """
        def dfs(rem):
            if rem == 0:
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in numSet:
                    curr.append(nums[i])
                    numSet.add(nums[i])
                    dfs(rem - 1)
                    curr.remove(nums[i])
                    numSet.remove(nums[i])
        dfs(len(nums))
        return res