class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        start = [-1, -1, -1]
        startIndex = -1
        for i in range(len(triplets)):
            t = triplets[i]
            valid = True
            for k in range(len(t)):
                if t[k] > target[k]:
                    valid = False
                    break
            if valid:
                start = t
                startIndex = i
                break
        if startIndex < 0:
            return False
        t1 = start
        for i in range(startIndex, len(triplets)):
            t2 = triplets[i]
            valid = True
            for k in range(3):
                if t2[k] > target[k]:
                    valid = False
                    break
            if valid:
                for k in range(3):
                    t1[k] = max(t1[k], t2[k])
                if t1 == target:
                    return True
        return False

            