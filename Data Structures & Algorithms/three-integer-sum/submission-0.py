class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            a = nums[i] * -1
            seenNums = {}
            for j in range(i + 1, len(nums)):
                b = nums[j]
                c = a - b
                #print("a : " + str(a))
                #print("b : " + str(b))
                #print("c : " + str(c))
                if c in seenNums:
                    res.add((nums[i], nums[j], c))
                    #print("res : ", res)
                seenNums[b] = j 
        newRes = [list(t) for t in res]
        return newRes