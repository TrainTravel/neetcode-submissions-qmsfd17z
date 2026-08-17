class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = -1
        
        while l < r:
            current_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, current_area)

            # move the shorter pointer of the two
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area