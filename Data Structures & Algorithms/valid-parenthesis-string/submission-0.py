class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        stars = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                elif stars > 0:
                    stars -= 1
                else:
                    return False
            elif c == '*':
                stars += 1
        stars = 0
        stack = []
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == ')':
                stack.append(c)
            elif c == '(':
                if stack:
                    stack.pop()
                elif stars > 0:
                    stars -= 1
                else:
                    return False
            elif c == '*':
                stars += 1
        return True


        
