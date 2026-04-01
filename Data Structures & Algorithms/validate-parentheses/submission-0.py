class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "{": "}", "[": "]"}

        stack = []
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if stack and ch == mapping[stack[-1]]:
                    stack.pop()
                    continue
                return False
        if stack:
            return False
        return True

