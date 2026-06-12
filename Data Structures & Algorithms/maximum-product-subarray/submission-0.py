class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #2 3 -2 1 -3 2 -4
    
        maxnum = 1
        minnum = 1
        res = float("-inf")
        for i, num in enumerate(nums):
            if num == 0:
                res = max(0, res)
                maxnum = 1
                minnum = 1
                continue
            tmp = maxnum*num
            maxnum = max(maxnum * num, minnum * num, num)
            minnum = min(tmp, minnum * num, num)
                

            res = max(maxnum, res)

        return res

        