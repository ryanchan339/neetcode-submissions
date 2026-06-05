class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(s)
        freq2 = Counter(t)
        for c in freq1.keys():
            if c not in freq2 or freq2[c] != freq1[c]:
                return False
        return len(freq1.keys()) == len(freq2.keys())