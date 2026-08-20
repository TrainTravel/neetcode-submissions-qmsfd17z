from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores INDICES (not values)
        l = r = 0

        while r < len(nums):
            # Step 1: Remove smaller elements from back
            # If current element is larger than back, remove back
            # (smaller elements can never be max while current exists)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Step 2: Add current index to deque
            q.append(r)

            # Step 3: Remove indices outside the window
            # If front index is before window start, remove it
            if l > q[0]:
                q.popleft()

            # Step 4: Record the answer once window is full
            # Window is full when we've processed k elements
            if (r + 1) >= k:
                output.append(nums[q[0]])  # Front is always the max
                l += 1
            
            r += 1

        return output