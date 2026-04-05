class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        unresolved = []

        for idx in range(len(temperatures)):
            # if not unresolved:
            #     unresolved.append(idx)
            #     print(unresolved)
            #     continue

            # [33, 32, 30]
            # [33, 32, 30, "38"]
            # when encountering 38, and the current stack is [33, 32, 30]
            # pop 30 -> then pop 32, then pop 33
            while(unresolved and temperatures[idx] > temperatures[unresolved[-1]]):
                ans[unresolved[-1]] = idx - unresolved[-1]
                print(f"meet {temperatures[idx]}, popping {temperatures[unresolved[-1]]}")
                unresolved.pop()

            unresolved.append(idx)
        return ans
