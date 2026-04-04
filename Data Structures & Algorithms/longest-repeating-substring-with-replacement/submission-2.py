class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        charMap = defaultdict(int)


        L, R = 0, 0
        max_freq = 0
        res = 0

        # constraint: window_length - max_freq <= k
        while R in range(len(s)):
            charMap[s[R]] += 1
            max_freq = max(max_freq, charMap[s[R]])

            # expand right until it breaks the constraint
            while(R - L + 1 - max_freq > k):
                charMap[s[L]] -= 1
                L += 1
                
            res = max(res, R - L + 1)
            R += 1
        return res