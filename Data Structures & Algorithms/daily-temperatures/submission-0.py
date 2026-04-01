class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ex. 30, 38, 30 36
        #.         8   0  6
        #.             -8. -2 ...
        #                  
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            print(f"current t: {t}")
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > t:
                    print(f"higher temp found {temperatures[j]}")
                    result[i] = j - i
                    break
        return result
            