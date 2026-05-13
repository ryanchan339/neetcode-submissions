class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        nstart, nend = newInterval
        appended = False
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if start > nend:
                res.append([nstart,nend])
                res.append(intervals[i])
                appended = True
                i += 1
                break
                
            elif not (nstart > end or start > nend):
                nstart = min(start, nstart)
                nend = max(end, nend)  
            else:
                res.append(intervals[i])
            i += 1
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        if not appended:
            res.append([nstart,nend])
        
        return res