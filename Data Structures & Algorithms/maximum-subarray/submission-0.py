class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = - math.inf
        curSum = maxSum
        for n in nums:
            curSum = max(curSum + n, n)
            maxSum = max(curSum, maxSum)
        return maxSum
        