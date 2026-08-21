class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        rows, cols = len(grid), len(grid[0])


        def dfs(row: int, col: int):
            # 1. STOP if out of bounds
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            
            # 2. STOP if this isn't land we want to visit
            if grid[row][col] == "0":
                return

            # 3. else it is a valid, sink it
            grid[row][col] = "0"
    
            # 4. continue dfs
            
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for col in range(cols):
            for row in range(rows):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        return count