class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        minSum = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        dp = [0] * COLS
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                # base case: bottom-right
                if r == ROWS -1 and c == COLS - 1:
                    dp[c] = grid[r][c]
                    continue

                if r == ROWS - 1: # r = 2
                    # dp[2] = cell(2, 1) + 3 or cell(1, 2) + 3
                    # dp[c] = dp[c + 1] + grid[r][c]
                    grid[r][c] += grid[r][c+1]
                    continue
                
                if c == COLS - 1:
                    # dp[c] = dp[c] + grid[r][c]
                    grid[r][c] += grid[r+1][c]
                    continue

                grid[r][c] += min(grid[r][c+1], grid[r+1][c])
                # dp[c] = grid[r][c] + min(dp[c], dp[c + 1])
        # return dp[0]
        return grid[0][0]
