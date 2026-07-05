class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        #stack ele - (index, height)
        for i in range(len(heights)):
            if not stack or stack[-1][1] <= heights[i]:
                stack.append((i, heights[i]))
            else:
                setIndex = i
                while stack and stack[-1][1] >= heights[i]:
                    top = stack.pop()
                    res = max(res, top[1] * (i - top[0]))
                    setIndex = top[0]
                stack.append((setIndex, heights[i]))
        while stack:
            top = stack.pop()
            res = max(res, top[1] * (len(heights) - top[0]))
    

        return res