class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}

        for c in s1:
            freq1[c] = freq1.get(c,0) + 1
        
     

        l = 0
        for r in range(len(s2)):
            if s2[r] not in freq1:
                l = r + 1
                freq2 = {}
                continue
            freq2[s2[r]] = freq2.get(s2[r], 0) + 1
            while freq2[s2[r]] > freq1[s2[r]]:
                freq2[s2[l]] -= 1
                l += 1
            if freq2 == freq1:
                return True

        return False
