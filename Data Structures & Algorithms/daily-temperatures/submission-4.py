class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] #storing indices that havent been answered
        for i, temp in enumerate(temperatures):
            while(stack and temperatures[stack[-1]] < temp): # pop until only unanswered indices are in stack
                # pop the newly answered index
                answered_idx = stack.pop()
                results[answered_idx] = i - answered_idx
           
            # store unresolved indices
            stack.append(i)
        return results