class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for c in s:
            if c.isalpha() or c.isdigit(): 
                ns += c
        ns = ns.lower()
        return ns == ns[::-1]