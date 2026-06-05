class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams.keys():
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        for k, v in anagrams.items():
            temp = []
            for a in v:
                temp.append(a)
            res.append(temp)
        return res