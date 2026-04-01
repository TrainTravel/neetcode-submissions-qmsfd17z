from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
            
        counter1 = Counter(s1)
        # Initialize the window with the first n1 characters
        counter2 = Counter(s2[:n1])
        
        # Check the first window
        if counter1 == counter2:
            return True

        # new window: i ~ i + n1 - 1        
        for i in range(1, n2 - n1 + 1):
            counter2[s2[i - 1]] -= 1
            
            counter2[s2[i + n1 - 1]] += 1

            if counter1 == counter2:
                return True
        return False
