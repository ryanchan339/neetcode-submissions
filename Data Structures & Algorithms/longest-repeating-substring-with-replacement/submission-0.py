class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        apple = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
        for c in apple:
            buf = k
            l = 0
            for r in range(len(s)):
                if s[r] != c:
                    buf -= 1
                while buf < 0 and l < r:
                    if s[l] != c:
                        buf += 1
                    l += 1
                res = max(res, r - l + 1)
        return res
