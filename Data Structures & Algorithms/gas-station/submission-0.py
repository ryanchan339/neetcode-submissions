class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        differences = []
        for i in range(len(gas)):
            differences.append(gas[i] - cost[i])
        currSum = 0
        l = 0
        currMax = 0

        for r in range(len(gas)):
            currSum += differences[r]
            if currSum < 0:
                l = r + 1
                currSum = 0
        return l
