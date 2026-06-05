class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            count = len(s)
            res += str(count)
            res += "#"
            res += s 
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            res.append(s[i:i+length])
            i += length
        return res
