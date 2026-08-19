class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        window_set = set(s[0])
        max_len = 1

        # expanding window by mv right pointer
        for r in range(l + 1, len(s)):
            # shrink: find duplicate, shrink window until a new unique non-duplicate substring opens up
            while s[r] in window_set:
                # shrinking window by advancing left pointer
                window_set.remove(s[l])
                l += 1

            # update current best
            max_len = max(max_len, r - l + 1)

            # print(window_set)
            # print("\n")
            # print(f"l moved to {l}, r: {r}")
            window_set.add(s[r])
        return max_len
