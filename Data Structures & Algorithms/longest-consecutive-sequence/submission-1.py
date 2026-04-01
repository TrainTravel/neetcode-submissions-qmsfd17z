from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq_dict = set(nums)

        max_len = 0
        cur_len = 0
        if not nums:
            return max_len

        for n in nums:
            cur_len = 0
            while(n in freq_dict):
                cur_len += 1
                n += 1
            max_len = max(max_len, cur_len)
        return max_len
