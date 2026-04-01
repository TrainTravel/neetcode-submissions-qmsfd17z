class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []


        # path as an accumulator
        def backtrack(start, path):
            # record current state
            res.append(list(path))

            for i in range(start, len(nums)):
                # make choice to include this num
                path.append(nums[i])

                # advance to next choice
                backtrack(i + 1, path)

                # undo the choice
                path.pop()

        backtrack(0, subset)
        return res
            