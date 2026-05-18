class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        res = []
        l = 0
        currFreq = {}
        for r in range(len(s)):
            currFreq[s[r]] = currFreq.get(s[r], 0) + 1
            valid = True
            for char, count in currFreq.items():
                if count < freq[char]:
                    valid = False
            if valid:
                res.append(r - l + 1)
                l = r + 1

        
        return res