class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()
        print(nums)

        def backtracking(start: int, subset: List[int]):
            result.append(subset.copy())

            for i in range(start, len(nums)):

                # check if this choice respects the boundary, only advance if it does
                if nums[i] > nums[i - 1] or i == start:
                    subset.append(nums[i])
                        
                    # next choice
                    backtracking(i + 1, subset.copy())

                    subset.pop()

        backtracking(0, subset)
        return result