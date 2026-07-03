class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #DDADOBECODEBANC
        
        smap = {}
        tmap = {}
        minimum = len(s)
        res = ""
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        l = 0
        for r in range(len(s)):
            smap[s[r]] = smap.get(s[r], 0) + 1
            valid = True
            for k, v in tmap.items():
                if k not in smap or smap[k] < tmap[k]:
                    valid = False
                    break
            if valid:
                while valid:
                    smap[s[l]] -= 1
                    l += 1 
                    for k, v in tmap.items():
                        if k not in smap or smap[k] < tmap[k]:
                            valid = False
                            break
                if r - l + 2 <= minimum:
                    minimum = r - l + 2
                    res = s[l - 1: r + 1]




        return res