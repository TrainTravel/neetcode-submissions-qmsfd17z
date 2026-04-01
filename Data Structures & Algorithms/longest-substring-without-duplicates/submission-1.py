class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A substring is consecutive subarray of the original string and can start from index 0 to len(s) - 1
        # of course brute force time complexity is quadratic
        # Because start and end indices are not known, this should be a sliding window of variable size problem

        l = 0
        curMax = 0
        # a set to record existing chars in current window
        curSet = set()

        for r in range(len(s)):
            while(s[r] in curSet): # constraint violated in the window
                #change window by shifting left pointer, while loop makes sure the shifts are done until constraint is ok
                # remove char of left pointer from set
                curSet.remove(s[l])
                l += 1
            # add char of new right pointer to set
            curSet.add(s[r])
            # update max
            curMax = max(curMax, r - l + 1)
        return curMax


            


        