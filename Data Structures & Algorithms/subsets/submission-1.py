class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # to store all the subsets
        ans = []
        global subset
        subset = []

        def dfs(idx: int, s: List[int]):
            # base case(leaf)
            if idx == len(nums):
                subset.append(s)
                return

            # starting at n
            # add the idx to path
            s.append(nums[idx])
            dfs(idx + 1, s.copy())
            
            # not to add the idx
            s.pop()

            # advance to next choice
            dfs(idx + 1, s.copy())

        # a for loop for each case of having the ith element as the start of the subset
        # for idx in range(len(nums)):
        dfs(0, subset.copy())
        return subset
