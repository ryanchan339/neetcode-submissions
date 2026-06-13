class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        i = 0
        currInterval = []
        currL = None
        currR = None
        while (i < len(intervals)):
            currL = intervals[i][0]
            currR = intervals[i][1]
            currInterval = [currL, currR]
            while i+1 < len(intervals):
                if intervals[i + 1][0] <= currR:
                    currInterval = [currL,max(intervals[i+1][1], currR)]
                    currR = max(intervals[i+1][1], currR)
                    i += 1
                else:
                    break
            res.append(currInterval)
            i += 1
        return res