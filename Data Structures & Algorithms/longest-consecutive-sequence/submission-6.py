class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_len = 0
        cur_len = 0
        if not nums:
            return max_len

        for n in s:
            cur_len = 0
            if n - 1 not in s:
                cur_len += 1
            
            while (n + cur_len) in s:
                cur_len += 1
            # print(list(range(n, n + cur_len - 1)))
            max_len = max(max_len, cur_len)
        return max_len
