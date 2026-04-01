class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ex. 30, 38, 30 36
        #.         8   0  6
        #.             -8. -2 ...
        #                  
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                val, idx = stack.pop()
                result[idx] = i - idx
            stack.append((temperatures[i], i))                
                

            # for j in range(i+1, len(temperatures)):
                # if temperatures[j] > t:
                    # print(f"higher temp found {temperatures[j]}")
                    # result[i] = j - i
                    # break
        return result
            