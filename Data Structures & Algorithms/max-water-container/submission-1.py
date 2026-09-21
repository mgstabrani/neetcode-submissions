class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l = 0
        r = len(heights) - 1
        while r > l:
            area = (r-l) * min(heights[r], heights[l])
            if area > maximum:
                maximum = area
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maximum
            