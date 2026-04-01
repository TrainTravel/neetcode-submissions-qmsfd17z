import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums1 = [-n for n in nums]
        heapq.heapify(nums1)
        # print(nums1)

        klargest = nums1[0]
        for i in range(k):
            klargest = heapq.heappop(nums1)

        return - klargest

        