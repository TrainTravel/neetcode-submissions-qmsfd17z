class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curMin = float('inf')
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while(curSum >= target):
                #shrink left pointer
                curMin = min(curMin, r - l + 1)
                curSum -= nums[l]
                l += 1

        return curMin if curMin != float('inf') else 0