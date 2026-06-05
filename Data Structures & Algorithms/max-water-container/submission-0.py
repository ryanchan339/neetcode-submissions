class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        second = len(height) - 1
        max_area = 0
        for i in range(len(height)):
            shorter_line = min(height[first], height[second])
            temp_area = shorter_line * (second - first)
            if temp_area > max_area:
                max_area = temp_area
            if height[first] > height[second]:
                second -= 1
            else:
                first += 1
        return max_area
