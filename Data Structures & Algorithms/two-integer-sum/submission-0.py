class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i, n in enumerate(nums):
            if target - n in map1:
                return [map1[target-n], i]
            
            map1[n] = i
        