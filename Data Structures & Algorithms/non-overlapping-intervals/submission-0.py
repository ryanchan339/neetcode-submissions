class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x : x[1])
        res = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            start1, end1 = curr
            start2, end2 = intervals[i]
            if not (end1 <= start2 or end2 <= start1):
                res += 1
            else:
                curr = intervals[i]
            
        return res

        