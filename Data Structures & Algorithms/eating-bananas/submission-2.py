import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [25,10,23,4], h = 4 -> output is bound to be 25 because it cannot be eaten in 4 hours with a rate of 24
        # piles = [1,4,3,2], h = 9 -> 1? 1 for index 0, 4 for index 1, 3 for 2, 2 for 3 -> 10 in total
        # s_min = min(piles)

        s_min = 1
        s_max = max(piles)
        res = s_max
        
        while s_min <= s_max:
            speed = (s_min + s_max) // 2
            
            hours = 0

            for i in piles:
                hours += math.ceil(i/speed)
            
            # decrease speed exploration to left half
            if hours <= h:
                res = speed
                s_max = speed - 1
            
            # increase speed exploration to right half
            else:
                s_min = speed + 1
        return res
                
