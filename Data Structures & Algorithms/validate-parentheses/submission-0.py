class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {')' : '(', '}' : '{', ']' : '['}
        for c in s:
            if c in chars:
                if len(stack) == 0 or stack[-1] != chars[c]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(c)
        return len(stack) == 0