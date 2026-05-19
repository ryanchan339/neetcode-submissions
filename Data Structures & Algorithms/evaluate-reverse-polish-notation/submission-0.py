class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for c in tokens:
            if c in operators:
                second = stack.pop()
                first = stack.pop()
                if c == '+':
                    stack.append(str(int(first) + int(second)))
                elif c == '-':
                    stack.append(str(int(first) - int(second)))
                elif c == '*':
                    stack.append(str(int(first) * int(second)))
                elif c == '/':
                    stack.append(str(math.trunc(int(first) / int(second))))
            else:
                stack.append(c)
        return int(stack[0])