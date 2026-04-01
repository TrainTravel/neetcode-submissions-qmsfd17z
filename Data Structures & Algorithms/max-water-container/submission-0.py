class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force would be O(n^2)
        # skip

        # two pointer
        l, r = 0, len(heights) - 1
        curMax = 0
        # curMax = min(heights[l], heights[r]) * (len(heights) - 1)
        # terminate when l == r
        # first intuition: only move the pointer of the shorter height?
        # what if the two are of same height? testcase 2
        while(l < r):
            # update curMax
            curMax = max(curMax, (r - l) * min(heights[l], heights[r]))
            if(heights[l] < heights[r]):
                # move and stop the left pointer to a taller height
                l += 1
            else:
                r -= 1
        return curMax

            