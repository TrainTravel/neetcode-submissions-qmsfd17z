class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest substring -> consecutive chars -> sliding window

        # k = 2
        # XYY -> {"X": 1, "Y": 2} => ans = 3
        # XYYX -> {"X": 2, "Y": 2} => ans = 4

        # k = 2
        # ABCDEFYYY => ans = 5, when R moves to the second Y(R = 7), L can be moved to the one and only E, so that the longest length is 4(L = 4) 
        # 7 - 4 + 1 = 4

        from collections import defaultdict

        charMap = defaultdict(int)

        L = 0
        charMap[s[L]] += 1
        max_freq_in_window = 1
        res = 1

        # only one distinct char in the window
        # constraint: window_length - max_freq_in_window <= k
        for R in range(1, len(s)):
            charMap[s[R]] += 1
            # print(f"L: {L}, R: {R}, charMap: {charMap}")
            max_freq_in_window = max(max_freq_in_window, charMap[s[R]])

            while (R - L + 1) - max_freq_in_window > k:
                # print(s[R])
                charMap[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res