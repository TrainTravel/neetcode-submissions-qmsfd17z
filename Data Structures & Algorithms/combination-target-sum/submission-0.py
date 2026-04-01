class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(start: int, current: List[int], remaining: int):
            if remaining == 0:
                res.append(current[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])
                current.pop()
            
        backtrack(0, subset, target)
        return res