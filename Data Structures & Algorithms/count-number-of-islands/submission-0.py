from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        # bfs
        M = len(grid)
        N = len(grid[0])

        visited = set()
        queue = deque()
        count = 0
        for m in range(M):
            for n in range(N):

                # discover any island in the queue if any, or if encountering a '1', add to the queue and continue exploring the current isalnd,
                # else stop and continue to the next spot if encountering a '0' continue
                if grid[m][n] == '1' and (m, n) not in visited:
                    queue.append((m, n))
                    visited.add((m, n))
                # loop until the first '1' is found(start of a new island)
                else:
                    continue

                while len(queue) > 0:
                    # Get the start position of this island 
                    i, j = queue.popleft()
                    # start exploring the four directions of the island
                    next_possible_positions = [(i + di, j + dj) for di, dj in directions]
                    
                    # add the next possible moves of this current position to the queue 
                    for next_i, next_j in next_possible_positions:
                        if 0 <= next_i < M and  0 <= next_j < N and (next_i, next_j) not in visited and grid[next_i][next_j] == '1':
                            queue.append((next_i, next_j))
                            visited.add((next_i, next_j))
                count += 1
        return count