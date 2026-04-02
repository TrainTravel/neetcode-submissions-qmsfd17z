class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def solve(ptr1: int, ptr2: int):
            if (ptr1, ptr2) in memo:
                return memo[(ptr1, ptr2)]

            if ptr1 == len(text1) or ptr2 == len(text2):
                memo[(ptr1, ptr2)] = 0
                return 0

            if text1[ptr1] == text2[ptr2]:
                print(f"ptr1: {ptr1}, ptr2: {ptr2}, {text1[ptr1]} == {text2[ptr2]}")
                memo[(ptr1, ptr2)] = 1 + solve(ptr1 + 1, ptr2 + 1)
                return memo[(ptr1, ptr2)]
            memo[(ptr1, ptr2)] = max(solve(ptr1 + 1, ptr2), solve(ptr1, ptr2 + 1))
            return memo[(ptr1, ptr2)]
        return solve(0, 0)