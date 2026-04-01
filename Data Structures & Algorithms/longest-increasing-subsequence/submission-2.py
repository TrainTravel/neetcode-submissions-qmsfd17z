class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # longest ending with index i
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                # If we can extend the LIS ending at j
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            #print(dp)
        return max(dp)