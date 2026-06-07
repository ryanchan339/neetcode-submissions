class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = 0, 0
        curr = []
        res = []
        def function(left, right):
            if (left == right == n):
                res.append("".join(curr))
                return
            if (right < left):
                curr.append(')')
                function(left, right + 1)
                curr.pop()
            if (left < n):
                curr.append('(')
                function(left + 1, right)
                curr.pop()

        function(left,right)
        return res
